"""
Author: Ryan Metcalf
Day:    5
Part:   2
"""

from pathlib import Path

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file
puzzle_lines = puzzle.read_text().splitlines()
seeds = [int(s) for s in ''.join(puzzle_lines.pop(0).split('seeds: ')).split()]
sep_indices = [i for i, x in enumerate(puzzle_lines) if x == ''] + [len(puzzle_lines)]
map_blocks = [[[int(a) for a in x.split()] for x in puzzle_lines[sep_indices[i]:sep_indices[i+1]][2:]] for i, s in enumerate(sep_indices) if s < len(puzzle_lines)]
locs = []

for s in seeds:
    sx = s
    for i, m in enumerate(map_blocks):
        big_diff = 0
        for row in m:
            dest, src, size = row
            diff = dest - src
            comp = src <= sx <= src + (size - 1)
            if comp:
                big_diff += diff
        sx += big_diff
    locs.append(sx)

def run():
    return min(locs)


if __name__ == '__main__':
    print(run())
