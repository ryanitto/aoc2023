"""
Author: Ryan Metcalf
Day:    4
Part:   1

https://adventofcode.com/2023/day/4#part1
"""

from pathlib import Path
from collections import Counter

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file
puzzle_lines = [l.lstrip('Card ') for l in puzzle.read_text().splitlines()]


class Card:

    def __init__(self, card_text):
        self.id, nums = card_text.split(': ')
        win_nums, my_nums = nums.split(' | ')
        self.win_nums = [int(n) for n in win_nums.split()]
        self.my_nums = [int(n) for n in my_nums.split()]
        self._matches = Counter()

    def my_matching_nums(self):
        for w in self.win_nums:
            if w in self.my_nums:
                self._matches.update({w: self.my_nums.count(w)})

    def get_points(self):
        points = 0
        self.my_matching_nums()
        if self._matches:
            points = 1
            for i, m in enumerate(self._matches):
                points *= 2 if i > 0 else 1
        return points


def run():
    total = 0
    for l in puzzle_lines:
        c = Card(l)
        c_pts = c.get_points()
        if c_pts:
            total += c_pts
    return total


if __name__ == '__main__':
    print(run())



