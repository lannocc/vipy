# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import clear_screen, get_terminal_size

from termcolor import cprint

import sys


class View(object):

    def __init__(self):
        # viewport width and height
        self.width, self.height = get_terminal_size()
        print("width = {}, height = {}".format(self.width, self.height))

        # all text is buffered to memory
        self.buf = []

        # current displayed buffer line (top of viewport)
        self.line = 0

        # current cursor position in viewport (x,y)
        self.cur = [0, 0]

    def load(self, filename):
        print("reading file: {}".format(filename))
        with open(filename, 'r') as f:
            self.buf = f.readlines()

    def draw(self):
        clear_screen()
        pos = [self.line, -1]

        for vrow in range(self.height - 1):
            if pos[0] >= len(self.buf):
                break

            for vcol in range(self.width):
                pos[1] += 1

                if pos[1] >= len(self.buf[pos[0]]):
                    pos[0] += 1
                    pos[1] = -1
                    print()
                    break

                c = self.buf[pos[0]][pos[1]]

                if c == '\r' or c == '\n':
                    continue

                if self.cur[0] == vcol and self.cur[1] == vrow:
                    #c = '\033[7m' + c + '\033[m'
                    cprint(c, color='magenta', on_color='on_cyan', attrs=["reverse"], end='')
                else:
                    print(c, end='')

        sys.stdout.flush()

