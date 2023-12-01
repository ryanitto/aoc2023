from pathlib import WindowsPath


class Puzzle(object):
    PUZZLE_FILE = 'puzzle.txt'

    def __init__(self, filepath=''):
        self.file = WindowsPath(filepath).parent / self.PUZZLE_FILE
        self.lines = self.file.read_text()

    def __str__(self):
        return self.lines

    def comma_line_to_ints(self):
        return [int(x) for x in self.lines[0].split(',')]

    def lines_as_int(self):
        return [int(line) for line in self.lines]

    def lines_as_float(self):
        return [float(line) for line in self.lines]
