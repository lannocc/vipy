# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import (
        hide_cursor, show_cursor,
        read_char,
        print_at )

import sys


def read_input(view):
    view.set_status('-- TYPING --')
    print_at(view.cursor[0]+1, view.cursor[1]+1, '', end='')
    show_cursor()

    while True:
        c = read_char()
        oc = ord(c)

        if oc == 3: # ctrl c
            return False

        elif oc == 26: # ctrl z
            # TODO: ask to save changes
            return False

        elif oc == 27:
            break

        else:
            print(c, end='')
            sys.stdout.flush()

    hide_cursor()
    view.clear_status()

    return True

