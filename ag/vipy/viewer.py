# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import clear_screen, get_terminal_size

from termcolor import cprint

import sys


class View(object):

    TAB_WIDTH = 4

    COLOR_NORMAL = 'white'
    BGCOLOR_NORMAL = 'blue'

    COLOR_CURSOR = 'magenta'
    BGCOLOR_CURSOR = 'cyan'
    ATTRS_CURSOR = ['reverse', 'bold', 'underline']

    COLOR_TAB = 'cyan'
    COLOR_NEW_LINE = 'green'
    COLOR_CARRIAGE_RETURN = 'yellow'
    COLOR_NO_TEXT = 'grey'

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
            self.reform()

    def reform(self, from_line=0):
        row = from_line

        while row < len(self.buf):
            line = self.buf[row]

            while len(line) >= self.width:
                self.buf.insert(row, line[:self.width])
                line = line[self.width:]
                row += 1

            self.buf[row] = line
            row += 1

    def get_print_width(self, line):
        w = 0

        for c in line:
            if c == '\t' or c == b'\t':
                w += self.TAB_WIDTH - (w % self.TAB_WIDTH)
            else:
                w += 1

        return w

    def draw(self):
        clear_screen()
        pos = [self.line, 0]

        for vrow in range(self.height - 1):
            vcol = 0

            while vcol < self.width:
                c = None
                cursor = False

                color = self.COLOR_NORMAL
                bgcolor = self.BGCOLOR_NORMAL
                attrs = None

                if pos[0] < len(self.buf) and pos[1] < len(self.buf[pos[0]]):
                    c = self.buf[pos[0]][pos[1]]

                if self.cur[0] == vcol and self.cur[1] == vrow:
                    cursor = True
                    color = self.COLOR_CURSOR
                    #bgcolor = self.BGCOLOR_CURSOR
                    attrs = self.ATTRS_CURSOR

                if c == '\r' or c == b'\r':
                    bgcolor = self.COLOR_CARRIAGE_RETURN
                    c = 'r' if cursor else ' '

                elif c == '\n' or c == b'\n':
                    bgcolor = self.COLOR_NEW_LINE
                    c = 'n' if cursor else ' '

                elif c == '\t' or c == b'\t':
                    bgcolor = self.COLOR_TAB
                    remains = ''.join([' ' for x in range(self.TAB_WIDTH - (vcol % self.TAB_WIDTH) - 1)])
                    c = ('t' if cursor else ' ') + remains

                elif not c:
                    bgcolor = self.COLOR_NO_TEXT
                    c = '$' if cursor else ' '

                if color or bgcolor or attrs:
                    cprint(c, color=color, on_color=('on_'+bgcolor) if bgcolor else None, attrs=attrs, end='')
                else:
                    print(c, end='')

                vcol += len(c)
                pos[1] += 1

            print()
            pos[0] += 1
            pos[1] = 0

        sys.stdout.flush()

