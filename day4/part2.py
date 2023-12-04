"""
Author: Ryan Metcalf
Day:    4
Part:   2

https://adventofcode.com/2023/day/4#part2
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
        self.matches = [w for w in self.win_nums if w in self.my_nums]
        self.copies = []

    def get_cards(self):
        return self.copies

    def __repr__(self):
        return f'Base #{self.id}'


class CopyCard(Card):
    def get_cards(self):
        result = []
        puzzle_line = int(self.id)
        lines = puzzle_lines[puzzle_line:puzzle_line+len(self.matches)]
        for l in lines:
            self.copies.append(CopyCard(l))
        return self.copies

    def __repr__(self):
        return f'Copy #{self.id}'


class OriginalCard(Card):
    def get_cards(self):
        result = []
        puzzle_line = int(self.id)
        lines = puzzle_lines[puzzle_line:puzzle_line+len(self.matches)]
        for l in lines:
            self.copies.append(CopyCard(l))
        return self.copies

    def __repr__(self):
        return f'Original #{self.id}'

total = 0


def traverse_copies(cards: list, parent: Card = None):
    global total
    if cards:
        total += len(cards)
    for c in cards:
        traverse_copies(c.get_cards(), parent=c)


def run():
    og_cards = [OriginalCard(l) for l in puzzle_lines]
    traverse_copies(og_cards)
    return total


if __name__ == '__main__':
    print(run())
