"""Checks that every example and model solution runs without crashing.

Run with `uv run pytest`. Scripts that ask for user input are given the
input listed in `INPUTS`. Where a script has a known correct answer, we also
check that it appears in the output (see `EXPECTED`).

Each script is run from a temporary copy of its own folder. This means that
scripts can read data files stored alongside them, and any files they write
don't end up in the repository. C++ examples and solutions are compiled and
run too, if a C++ compiler is available.

Test files written for the lesson on testing (`test_*.py`) are also run with
pytest, to check that they pass (or, in one case, fail on purpose).

Scripts that use `numpy` or `matplotlib` are skipped unless the `scientific`
dependency group is installed. To include them, run
`uv run --group scientific pytest`.
"""
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

LESSONS_DIR = Path(__file__).parent.parent / "lessons"

# Rows and columns for noughts and crosses games (one number per line)
NOUGHTS_AND_CROSSES_WIN = "0\n0\n1\n0\n0\n0\n0\n1\n1\n1\n0\n2\n"
NOUGHTS_AND_CROSSES_DRAW = "0\n0\n0\n1\n0\n2\n1\n1\n1\n0\n1\n2\n2\n1\n2\n0\n2\n2\n"

FILMS = "Spirited Away\nPaddington 2\nThe Matrix\nUp\nArrival\n"

# Simulated user input for interactive scripts (one line per `input` call)
INPUTS = {
    # Lesson 1
    "01-variables-and-types/examples/fav_fruit.py": "mango\n",
    "01-variables-and-types/solutions/task5_triangle_area_input.py": "6\n9\n",
    "01-variables-and-types/solutions/task7_temperature.py": "100\n",
    "01-variables-and-types/solutions/task8_minutes_and_seconds.py": "200\n",
    "01-variables-and-types/solutions/task9_coins.py": "388\n",
    # Lesson 2
    "02-conditionals/solutions/task1_odd_or_even.py": "7\n",
    "02-conditionals/solutions/task2_grades.py": "79\n",
    "02-conditionals/solutions/task3_cinema_tickets.py": "65\n",
    "02-conditionals/solutions/task4_maths_quiz.py": "1\n1\n3\n",
    "02-conditionals/solutions/task5_leap_year.py": "1900\n",
    "02-conditionals/solutions/task6_rock_paper_scissors.py": "rock\n",
    "02-conditionals/solutions/task7_rock_paper_scissors_short.py": "rock\n",
    # Lesson 3
    "03-loops/solutions/task2_times_tables.py": "7\n",
    "03-loops/solutions/task3_sum_to_n.py": "4\n",
    "03-loops/solutions/task4_count_vowels.py": "Hello World\n",
    "03-loops/solutions/task5_validate_input.py": "0\n11\n5\n",
    "03-loops/solutions/task6_guess_the_number.py": "".join(f"{i}\n" for i in range(1, 101)),
    "03-loops/solutions/task8_rock_paper_scissors_loop.py": "rock\nlizard\npaper\nquit\n",
    "03-loops/solutions/task9_star_patterns.py": "4\n",
    # Lesson 4
    "04-lists/solutions/task4_linear_search.py": "Grace\n",
    "04-lists/solutions/task5_above_average.py": "3\n5\n10\ndone\n",
    "04-lists/solutions/task8_lottery.py": "1\n2\n3\n4\n5\n6\n",
    # Lesson 5 (X takes a square that's already taken, then wins along the top row)
    "05-2d-lists/solutions/task5_noughts_and_crosses.py": NOUGHTS_AND_CROSSES_DRAW,
    "05-2d-lists/solutions/task6_noughts_and_crosses_winner.py": NOUGHTS_AND_CROSSES_WIN,
    # Lesson 6
    "06-functions/solutions/task4_temperature_converter.py": "1\n100\n",
    "06-functions/solutions/task5_get_int_in_range.py": "200\n30\n0\n7\n",
    "06-functions/solutions/task7_noughts_and_crosses.py": NOUGHTS_AND_CROSSES_WIN,
    # Lesson 7
    "07-strings/solutions/task1_name_slicing.py": "Ada\nLovelace\n",
    "07-strings/solutions/task4_password_checker.py": "password\nPassw0rd\n",
    "07-strings/solutions/task5_word_stats.py": "The quick brown fox jumps over the lazy dog\n",
    # Lesson 8
    "08-exceptions/examples/traceback_example.py": "30\n",
    "08-exceptions/examples/try_except_else_finally.py": "4\n",
    "08-exceptions/solutions/task2_get_int.py": "abc\n4\n5\n",
    "08-exceptions/solutions/task3_safe_division.py": "6\n4\n",
    "08-exceptions/solutions/task4_guess_the_number.py": "x\n200\n" + "".join(f"{i}\n" for i in range(1, 101)),
    "08-exceptions/solutions/task5_menu.py": "0\n",
    "08-exceptions/solutions/task7_bmi.py": "70\n1.75\n",
    # Lesson 9
    "09-files/solutions/task2_write_films.py": FILMS,
    "09-files/solutions/task3_diary.py": "Not bad\n",
    "09-files/solutions/task5_high_scores.py": "Bailey\n8000\n",
    "09-files/solutions/task6_file_stats.py": "poem.txt\n",
    # Lesson 11
    "11-classes-and-objects/solutions/task9_higher_or_lower.py": "h\n" * 60,
    # Lesson 13
    "13-dictionaries-and-sets/solutions/task1_phone_book.py": "1\nAda\n0123\n2\nAda\n2\nTim\n3\nTim\n4\n9\n5\n",
    # Lesson 14
    "14-packages/solutions/task2_birthday.py": "12\n25\n",
}

# Scripts that need another script to run first, e.g. to create a file they read
RUN_FIRST = {
    "09-files/solutions/task2_read_films.py": "09-files/solutions/task2_write_films.py",
    "09-files/solutions/task8_decrypt_file.py": "09-files/solutions/task8_encrypt_file.py",
}

# Text that must appear in the output of scripts with a known answer
EXPECTED = {
    "00-getting-started/solutions/task1_hello_world.py": "Hello world",
    "01-variables-and-types/solutions/task1_triangle_area.py": "27.0",
    "01-variables-and-types/solutions/task5_triangle_area_input.py": "Area = 27.0 cm^2",
    "01-variables-and-types/solutions/task7_temperature.py": "212.0 °F",
    "01-variables-and-types/solutions/task8_minutes_and_seconds.py": "3 minutes and 20 seconds",
    "02-conditionals/solutions/task2_grades.py": "grade B",
    "02-conditionals/solutions/task3_cinema_tickets.py": "£5",
    "02-conditionals/solutions/task5_leap_year.py": "1900 is not a leap year",
    "03-loops/solutions/task3_sum_to_n.py": "is 10",
    "03-loops/solutions/task4_count_vowels.py": "contains 3 vowels",
    "03-loops/solutions/task10_primes.py": "97",
    "04-lists/solutions/task3_temperatures.py": "Mean: 21.1",
    "04-lists/solutions/task4_linear_search.py": "Found Grace at index 2",
    "04-lists/solutions/task7_remove_duplicates.py": "['red', 'blue', 'green', 'yellow']",
    "04-lists/solutions/task9_second_largest.py": "second largest number is 38",
    "05-2d-lists/solutions/task3_test_scores.py": "Alan has the highest mean score",
    "05-2d-lists/solutions/task4_matrix_addition.py": "[44, 55, 66]",
    "05-2d-lists/solutions/task5_noughts_and_crosses.py": "It's a draw!",
    "05-2d-lists/solutions/task6_noughts_and_crosses_winner.py": "Player X wins!",
    "05-2d-lists/solutions/task7_matrix_multiplication.py": "[43, 50]",
    "06-functions/solutions/task6_list_functions.py": "73.8",
    "06-functions/solutions/task7_noughts_and_crosses.py": "Player X wins!",
    "06-functions/solutions/task8_is_prime.py": "71",
    "07-strings/solutions/task6_caesar_cipher.py": "Khoor, Zruog!",
    "07-strings/solutions/task7_receipt.py": "£8.55",
    "07-strings/solutions/task8_run_length_encoding.py": "12W1B3W",
    "08-exceptions/solutions/task5_menu.py": "between 1 and 5",
    "08-exceptions/solutions/task7_bmi.py": "22.9",
    "08-exceptions/solutions/task9_fixed_scores.py": "Number of passes: 5",
    "08-exceptions/solutions/task10_mean_of_valid.py": "5.35",
    "09-files/solutions/task1_line_numbers.py": "11: -- Christina Rossetti",
    "09-files/solutions/task2_read_films.py": "5. Arrival",
    "09-files/solutions/task4_read_scores.py": "Highest score: Alan (90)",
    "09-files/solutions/task5_high_scores.py": "3. Bailey",
    "09-files/solutions/task6_file_stats.py": "11 lines, 45 words and 238 characters",
    "09-files/solutions/task7_weather.py": "Hottest day: 2026-07-11 (29.1 °C)",
    "09-files/solutions/task8_decrypt_file.py": "Meet me by the old oak tree at midnight.",
    "09-files/solutions/task9_csv_module.py": "Turing, Alan's favourite food is fish, chips and mushy peas",
    "10-searching-and-sorting/solutions/task2_binary_search.py": "Binary search: 19 comparisons",
    "10-searching-and-sorting/solutions/task4_bubble_sort.py": "After pass 4: [1, 2, 4, 6, 9]",
    "10-searching-and-sorting/solutions/task7_merge.py": "[1, 2, 3, 4, 6, 7, 8, 9]",
    "10-searching-and-sorting/solutions/task9_merge_sort.py": "[1, 2, 3, 4, 6, 7, 8, 9]",
    "11-classes-and-objects/solutions/task3_bank_account.py": "Ada's account: £120.50",
    "11-classes-and-objects/solutions/task4_students.py": "Alan has the highest mean score",
    "11-classes-and-objects/solutions/task6_cards.py": "47 cards left",
    "11-classes-and-objects/solutions/task7_class_variables.py": "Alan's account: £288.75",
    "11-classes-and-objects/solutions/task8_static_methods.py": "5 5 25 True",
    "11-classes-and-objects/solutions/task10_vector.py": "(4, 6)",
    "12-inheritance-and-encapsulation/examples/bank_account.cpp": "Ada's balance is £157.5",
    "12-inheritance-and-encapsulation/solutions/task1_shapes.py": "A square with area 25.00",
    "12-inheritance-and-encapsulation/solutions/task2_employees.py": "Grace: £5,000.00 per month",
    "12-inheritance-and-encapsulation/solutions/task5_bank_account.py": "has no setter",
    "12-inheritance-and-encapsulation/solutions/task6_temperature.py": "below absolute zero",
    "12-inheritance-and-encapsulation/solutions/task8_car_and_garage.py": "EV24 ZAP (283 hp, 18\" wheels)",
    "12-inheritance-and-encapsulation/solutions/task9_rectangle.cpp": "Height is still: 4",
    "12-inheritance-and-encapsulation/solutions/task10_abstract_shapes.py": "Can't instantiate abstract class Triangle",
    "13-dictionaries-and-sets/solutions/task1_phone_book.py": "Sorry, Tim isn't in the phone book",
    "13-dictionaries-and-sets/solutions/task2_word_frequency.py": "the: 6",
    "13-dictionaries-and-sets/solutions/task3_scrabble.py": "python: 14",
    "13-dictionaries-and-sets/solutions/task5_favourite_films.py": "Both like: ['Arrival', 'The Matrix', 'Up']",
    "13-dictionaries-and-sets/solutions/task8_anagram_groups.py": "stone, tones, notes, onset",
    "13-dictionaries-and-sets/solutions/task9_morse_code.py": "HELLO WORLD",
    "15-type-hints-and-dataclasses/solutions/task3_student_dataclass.py": "Alan has the highest mean score",
    "15-type-hints-and-dataclasses/solutions/task4_point.py": "cannot assign to field 'x'",
    "15-type-hints-and-dataclasses/solutions/task5_shop.py": "Total stock value: £238.00",
    "15-type-hints-and-dataclasses/solutions/task6_library.py": "is already on loan",
    "14-packages/solutions/task1_use_shapes.py": "314.16",
    "14-packages/solutions/task4_numpy_temperatures.py": "Days warmer than 20 °C: 4",
    "16-recursion-stacks-and-queues/solutions/task1_factorial.py": "5000! has 16,326 digits",
    "16-recursion-stacks-and-queues/solutions/task2_recursion_practice.py": "olleh",
    "16-recursion-stacks-and-queues/solutions/task3_fibonacci.py": "That took 242,785 calls!",
    "16-recursion-stacks-and-queues/solutions/task6_balanced_brackets.py": "'(a[b)]': False",
    "16-recursion-stacks-and-queues/solutions/task8_memoised_fibonacci.py": "That took 49 calls",
    "16-recursion-stacks-and-queues/solutions/task9_towers_of_hanoi.py": "5 discs took 31 moves",
    "16-recursion-stacks-and-queues/solutions/task10_circular_queue.py": "['E', 'F', 'C', 'D'] (front=2, rear=2)",
    "18-linked-lists/solutions/task1_days_of_the_week.py": "There are 7 nodes in the list",
    "18-linked-lists/solutions/task3_insert_after.py": "3 -> 8 -> 7 -> 5 -> 9",
    "18-linked-lists/solutions/task4_delete.py": "8 -> 2",
    "18-linked-lists/solutions/task6_doubly_linked_list.py": "['B'] ['B']",
    "18-linked-lists/solutions/task7_pass_the_parcel.py": "Ada wins!",
    "18-linked-lists/solutions/task8_array_linked_list.py": "[8, 5, 7]",
    "18-linked-lists/solutions/task9_reverse.py": "5 -> 4 -> 3 -> 2 -> 1",
    "19-binary-search-trees/solutions/task3_traversals.py": "[1, 4, 7, 6, 3, 13, 14, 10, 8]",
    "19-binary-search-trees/solutions/task4_height.py": "3",
    "19-binary-search-trees/solutions/task5_delete.py": "After deleting 8: [1, 4, 6, 7, 10]",
    "19-binary-search-trees/solutions/task7_breadth_first.py": "[8, 3, 10, 1, 6, 14, 4, 7, 13]",
    "19-binary-search-trees/solutions/task8_balanced_trees.py": "Height when built balanced: 9",
    "20-hash-tables-and-sets/solutions/task2_chaining.py": "[['Guido', 204], ['Margaret', 217]]",
    "20-hash-tables-and-sets/solutions/task3_linear_probing.py": "['Guido', 'Margaret', 'Alan', 'Ada', 'Tim', None, 'Grace']",
    "20-hash-tables-and-sets/solutions/task4_resizing.py": "20 items: size 32, load factor 0.62",
    "20-hash-tables-and-sets/solutions/task5_hash_set.py": "[1, 2, 3, 4]",
    "20-hash-tables-and-sets/solutions/task6_prerequisites.py": "['Data Structures', 'Maths 1']",
    "20-hash-tables-and-sets/solutions/task8_hashable_points.py": "origin",
}

# Lesson test files that are meant to fail, because they find a bug
EXPECTED_TEST_FAILURES = {
    "17-testing/examples/test_leap_year.py",
}

# Scripts that are meant to end with an exception, and the exception they raise
EXPECTED_ERRORS = {
    "12-inheritance-and-encapsulation/examples/name_mangling.py": "AttributeError",
}

# Scripts that can't be tested automatically
SKIP = {
    "08-exceptions/examples/bare_except.py",  # deliberately can't be stopped
}


def find_scripts(extension: str) -> list[str]:
    """Finds all examples and model solutions with the given file extension,
    relative to `LESSONS_DIR`"""
    scripts = [
        *LESSONS_DIR.glob(f"*/examples/*{extension}"),
        *LESSONS_DIR.glob(f"*/solutions/*{extension}"),
    ]
    relative_paths = (path.relative_to(LESSONS_DIR).as_posix() for path in scripts)
    return sorted(path for path in relative_paths if path not in SKIP)


def needs_missing_packages(script: str) -> bool:
    """Checks whether a script uses `numpy` or `matplotlib` when they aren't
    installed"""
    source = (LESSONS_DIR / script).read_text(encoding="utf-8")
    for package in ["numpy", "matplotlib"]:
        if f"import {package}" in source and importlib.util.find_spec(package) is None:
            return True
    return False


def run_python(script: str, run_dir: Path) -> subprocess.CompletedProcess:
    """Runs a Python script from `run_dir`, giving it any input in `INPUTS`"""
    return subprocess.run(
        [sys.executable, Path(script).name],
        cwd=run_dir,
        input=INPUTS.get(script, ""),
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=30,
        env={**os.environ, "MPLBACKEND": "Agg"},  # draw graphs without opening windows
    )


@pytest.mark.parametrize("script", find_scripts(".py"))
def test_script_runs(script: str, tmp_path: Path) -> None:
    if needs_missing_packages(script):
        pytest.skip("needs the `scientific` dependency group")

    run_dir = tmp_path / "run"
    shutil.copytree((LESSONS_DIR / script).parent, run_dir)

    if script in RUN_FIRST:
        first = run_python(RUN_FIRST[script], run_dir)
        assert first.returncode == 0, first.stderr

    result = run_python(script, run_dir)
    if script in EXPECTED_ERRORS:
        assert EXPECTED_ERRORS[script] in result.stderr
    else:
        assert result.returncode == 0, result.stderr
    if script in EXPECTED:
        assert EXPECTED[script] in result.stdout


@pytest.mark.skipif(shutil.which("g++") is None, reason="no C++ compiler found")
@pytest.mark.parametrize("program", find_scripts(".cpp"))
def test_cpp_program_runs(program: str, tmp_path: Path) -> None:
    executable = tmp_path / "program"
    compiled = subprocess.run(
        ["g++", "-std=c++17", "-Wall", "-Werror", str(LESSONS_DIR / program), "-o", str(executable)],
        capture_output=True,
        text=True,
    )
    assert compiled.returncode == 0, compiled.stderr

    result = subprocess.run([str(executable)], capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr
    if program in EXPECTED:
        assert EXPECTED[program] in result.stdout


def test_type_hints(tmp_path: Path) -> None:
    """Checks the type hints in the lesson on type hints using mypy"""
    lesson_dir = LESSONS_DIR / "15-type-hints-and-dataclasses"
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", "--cache-dir", str(tmp_path), "examples", "solutions"],
        cwd=lesson_dir,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout


def find_lesson_tests() -> list[str]:
    """Finds the `test_*.py` files in the lessons, relative to `LESSONS_DIR`"""
    tests = [
        *LESSONS_DIR.glob("*/examples/test_*.py"),
        *LESSONS_DIR.glob("*/solutions/test_*.py"),
    ]
    return sorted(path.relative_to(LESSONS_DIR).as_posix() for path in tests)


@pytest.mark.parametrize("test_file", find_lesson_tests())
def test_lesson_tests(test_file: str, tmp_path: Path) -> None:
    run_dir = tmp_path / "run"
    shutil.copytree((LESSONS_DIR / test_file).parent, run_dir)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider", Path(test_file).name],
        cwd=run_dir,
        capture_output=True,
        text=True,
    )
    if test_file in EXPECTED_TEST_FAILURES:
        assert result.returncode == 1, result.stdout  # 1 means "some tests failed"
    else:
        assert result.returncode == 0, result.stdout
