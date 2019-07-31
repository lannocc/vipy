# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import (
        clear_screen,
        hide_cursor, show_cursor,
        print_at, cprint, cprint_at,
        get_terminal_size )

import sys
import copy


class TerminalView():

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

        self.rows = []      # lines currently visible
        self.cursor = [0,0] # screen cursor [row,col]
        self.status = ''    # status text (bottom of screen area)

    def fill(self, buf):
        row = []

        for p in buf:
            row.append(p)

            if len(row) >= self.width or p.c == '\n':
                self.rows.append(row)

                if len(self.rows) >= self.height - 1:
                    break

                row = []

            elif p.c == '\t':
                size = self.TAB_WIDTH - (len(row)-1) % self.TAB_WIDTH

                p = copy.copy(p)
                p.continuation = True

                while size > 1 and len(row) < self.width:
                    row.append(p)
                    size -= 1

    def refresh(self):
        hide_cursor()
        clear_screen()

        for vrow in range(self.height - 1):
            for vcol in range(self.width):
                self.refresh_char(vrow, vcol, move=False)

        sys.stdout.flush()

    def set_status(self, text):
        row = self.height
        diff = len(self.status) - len(text)
        end = ' ' * diff if diff > 0 else ''

        print_at(row, 1, text, end=end)

        if diff > 0:
            # reset terminal cursor position
            print_at(row, len(text) + 1, '', end='')

        sys.stdout.flush()
        self.status = text

    def clear_status(self):
        self.set_status('')

    def move_cursor(self, row, col):
        old_row, old_col = self.cursor
        self.cursor = [row, col]

        self.refresh_char(old_row, old_col)
        self.refresh_char(row, col)

        sys.stdout.flush()

    def move_left(self):
        if self.cursor[1] > 0:
            self.move_cursor(self.cursor[0], self.cursor[1] - 1)

    def move_right(self):
        if self.cursor[1] < self.width - 1:
            self.move_cursor(self.cursor[0], self.cursor[1] + 1)

    def move_up(self):
        if self.cursor[0] > 0:
            self.move_cursor(self.cursor[0] - 1, self.cursor[1])

    def move_down(self):
        if self.cursor[0] < self.height - 1:
            self.move_cursor(self.cursor[0] + 1, self.cursor[1])

    def refresh_char(self, row, col, move=True):
        p = None
        c = None
        cursor = False

        color = self.COLOR_NORMAL
        bgcolor = self.BGCOLOR_NORMAL
        attrs = None

        if row < len(self.rows) and col < len(self.rows[row]):
            p = self.rows[row][col]
            c = p.c

        if self.cursor[0] == row and self.cursor[1] == col:
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
            c = 't' if cursor and not p.continuation else ' '

        elif not c:
            bgcolor = self.COLOR_NO_TEXT
            c = '$' if cursor else ' '

        if color or bgcolor or attrs:
            on_color = ('on_'+bgcolor) if bgcolor else None 
            if move:
                cprint_at(row+1, col+1, c, color=color, on_color=on_color, attrs=attrs, end='')
            else:
                cprint(c, color=color, on_color=on_color, attrs=attrs, end='')
        else:
            if move:
                print_at(row+1, col+1, c, end='')
            else:
                print(c, end='')

    def close(self):
        show_cursor()

