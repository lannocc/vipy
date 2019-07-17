# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@


class MemoryBuffer():

    def __init__(self):
        self.lines = []     # memory buffer of characters by line
        self.cursor = [0,0] # character cursor [line,index]

    def load(self, filename):
        print("reading file: {}".format(filename))

        with open(filename, 'r') as f:
            self.lines = f.readlines()

    def populate(self, view):
        rows = []

        for line in self.lines:
            start = 0

            while len(rows) < view.height - 1:
                row, start = view.build_row(line, start)
                rows.append(row)

                if not start:
                    break

        view.rows = rows

