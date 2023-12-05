"""
Author: Ryan Metcalf
Day:    3
Part:   2
"""

from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file

def run():
    return puzzle


if __name__ == '__main__':
    print(run())
