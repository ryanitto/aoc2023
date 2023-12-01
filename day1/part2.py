"""
Author: Ryan Metcalf
Day:    1
Part:   1

--- Day 1: Trebuchet?! ---
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""

from pathlib import Path
import re

num_map = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9
}

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file
puzzle_lines = puzzle.read_text().split()

def run():
    num_positions = []
    for i, p in enumerate(puzzle_lines):
        num_dict = {}
        for k, v in num_map.items():
            for a in re.finditer(str(k), p):
                num_dict[a.start()] = v
        num_positions.append(num_dict)

    total = sum([int(f'{p[min(p)]}{p[max(p)]}') for p in num_positions])
    return total


if __name__ == '__main__':
    print(run())
