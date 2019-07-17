# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import (
        clear_screen,
        hide_cursor, show_cursor,
        print_at,
        get_terminal_size,
        cprint )

import sys


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
        #self.buf = buf      # the full content buffer
        self.cursor = [0,0] # screen cursor [row,col]
        self.status = ''    # status text (bottom of screen area)

    def refresh(self):
        hide_cursor()
        clear_screen()

        # the content buffer must conform to our view size and settings
        #self.buf.reform(self)

        self.print_all()

    def print_all(self):
        #for row in self.rows:
        #    print(row, end='')

        for vrow in range(self.height - 1):

            for vcol in range(self.width):
                c = None
                cursor = False

                color = self.COLOR_NORMAL
                bgcolor = self.BGCOLOR_NORMAL
                attrs = None

                if vrow < len(self.rows) and vcol < len(self.rows[vrow]):
                    c = self.rows[vrow][vcol]

                if self.cursor[0] == vcol and self.cursor[1] == vrow:
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
                    #remains = ''.join([' ' for x in range(self.TAB_WIDTH - (vcol % self.TAB_WIDTH) - 1)])
                    c = ('t' if cursor else ' ') #+ remains

                elif not c:
                    bgcolor = self.COLOR_NO_TEXT
                    c = '$' if cursor else ' '

                if color or bgcolor or attrs:
                    cprint(c, color=color, on_color=('on_'+bgcolor) if bgcolor else None, attrs=attrs, end='')
                else:
                    print(c, end='')

        sys.stdout.flush()

    def set_status(self, text):
        row = self.height
        diff = len(self.status) - len(text)
        end = ' ' * diff if diff > 0 else ''

        print_at(row, 0, text, end=end)

        if diff > 0:
            # reset terminal cursor position
            print_at(row, len(text) + 1, '', end='')

        sys.stdout.flush()
        self.status = text

    def clear_status(self):
        self.set_status('')

    def build_row(self, text, start=0):
        row = ''
        col = 0

        for i in range(start, len(text)):
            c = text[i]
            row += c

            if c == '\t':
                size = self.TAB_WIDTH - col % self.TAB_WIDTH
                col += size # FIXME: check against self.width here too

                if size > 1:
                    row += ' ' * (size - 1)

            else:
                col += 1

            if col >= self.width:
                return row, i + 1

        return row, None

    def close(self):
        show_cursor()

