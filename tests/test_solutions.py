"""Checks that every example and model solution runs without crashing.

Run with `uv run pytest`. Scripts that ask for user input are given the
input listed in `INPUTS`. Where a script has a known correct answer, we also
check that it appears in the output (see `EXPECTED`).
"""
import subprocess
import sys
from pathlib import Path

import pytest

LESSONS_DIR = Path(__file__).parent.parent / "lessons"

# Rows and columns for noughts and crosses games (one number per line)
NOUGHTS_AND_CROSSES_WIN = "0\n0\n1\n0\n0\n0\n0\n1\n1\n1\n0\n2\n"
NOUGHTS_AND_CROSSES_DRAW = "0\n0\n0\n1\n0\n2\n1\n1\n1\n0\n1\n2\n2\n1\n2\n0\n2\n2\n"

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
    "08-exceptions/solutions/task8_mean_of_valid.py": "5.35",
}

# Scripts that can't be tested automatically
SKIP = {
    "08-exceptions/examples/bare_except.py",  # deliberately can't be stopped
}


def find_scripts() -> list[str]:
    """Finds all examples and model solutions, relative to `LESSONS_DIR`"""
    scripts = [
        *LESSONS_DIR.glob("*/examples/*.py"),
        *LESSONS_DIR.glob("*/solutions/*.py"),
    ]
    relative_paths = (path.relative_to(LESSONS_DIR).as_posix() for path in scripts)
    return sorted(path for path in relative_paths if path not in SKIP)


@pytest.mark.parametrize("script", find_scripts())
def test_script_runs(script: str) -> None:
    result = subprocess.run(
        [sys.executable, script],
        cwd=LESSONS_DIR,
        input=INPUTS.get(script, ""),
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    if script in EXPECTED:
        assert EXPECTED[script] in result.stdout
