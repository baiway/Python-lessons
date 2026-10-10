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
}


def find_scripts() -> list[str]:
    """Finds all examples and model solutions, relative to `LESSONS_DIR`"""
    scripts = [
        *LESSONS_DIR.glob("*/examples/*.py"),
        *LESSONS_DIR.glob("*/solutions/*.py"),
    ]
    return sorted(str(path.relative_to(LESSONS_DIR)) for path in scripts)


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
