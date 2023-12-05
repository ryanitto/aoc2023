"""
Author: Ryan Metcalf
Day:    3
Part:   1
"""

from pathlib import Path
import re
import numpy

puzzle = Path(__file__).parent / 'puzzle.txt'  # .txt file next to .py file
puzzle_lines = puzzle.read_text().splitlines()
lines_to_lists = [list(p) for p in puzzle_lines]

grid = numpy.array(lines_to_lists)[0][0]
print(grid[0][0])
numpy.str_.clip

num_ranges = {int(k): [] for k, _ in enumerate(puzzle_lines)}
sym_ranges = {k: [] for k in num_ranges}
valid_nums = []

def run():
    for i, p in enumerate(puzzle_lines):
        f = re.finditer(r'\d*', p)
        for it in f:
            if it.start() != it.end():
                num_ranges[i].append([it.start(), it.end()])
        s = re.finditer(r'[^\.\w]', p)
        for st in s:
            if st.start() != st.end():
                sym_ranges[i].append([st.start(), st.end()])

    for k, v in num_ranges.items():
        if not v:
            continue
        upper_line = k-1 if k > 0 else None
        lower_line = k+1 if k < len(num_ranges)-1 else None
        for r in v:
            num = int(puzzle_lines[k][r[0]:r[1]])
            num_start, num_end = r
            if upper_line:
                for s in sym_ranges[upper_line]:
                    sym_start, sym_end = s
                    starts = sym_start == num_start or sym_start == num_start - 1 or sym_start == num_start + 1
                    ends = sym_end == num_end or sym_end == num_end + 1 or sym_end == num_end - 1
                    if starts or ends:
                        print(f'yes - {num} - {puzzle_lines[upper_line][sym_start:sym_end]}')
                        valid_nums.append(num)

            print(r, num, k, sym_ranges[k])
            for s in sym_ranges[k]:
                sym_start, sym_end = s
                starts = sym_start == num_start or sym_start == num_start - 1
                ends = sym_end == num_end or sym_end == num_end + 1
                if starts or ends:
                    print(f'yes - {num} - {puzzle_lines[k][sym_start:sym_end]}')
                    valid_nums.append(num)
                print(r, num, upper_line, sym_ranges[k])

            if lower_line:
                for s in sym_ranges[lower_line]:
                    sym_start, sym_end = s
                    starts = sym_start == num_start or sym_start == num_start - 1
                    ends = sym_end == num_end or sym_end == num_end + 1
                    if starts or ends:
                        print(f'yes - {num} - {puzzle_lines[lower_line][sym_start:sym_end]}')
                        valid_nums.append(num)
                print(r, num, lower_line, sym_ranges[lower_line])

    print(num_ranges)
    print(sym_ranges)
    print(valid_nums)
    total = sum(valid_nums)
    return total

def run():
    return


if __name__ == '__main__':
    print(run())
