# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import (
        read_char,
        hide_cursor, show_cursor )

import sys


def read_command(view):
    view.set_status(':')
    show_cursor()

    cmd = None

    while True:
        c = read_char()
        oc = ord(c)

        if oc == 3: # ctrl c
            return False

        elif oc == 26: # ctrl z
            # TODO: ask to save changes
            return False

        elif oc == 27: # escape
            break

        elif oc == 127: # backspace
            if not cmd:
                break

            cmd = cmd[:-1]
            view.set_status(':{}'.format(cmd))

        elif c == '\r' or c == b'\r' or c == '\n' or c == b'\n':
            if cmd and len(cmd) > 0:
                if cmd == 'q' or cmd == b'q' or cmd == 'q!' or cmd == b'q!':
                    return False

            break

        else:
            if cmd:
                cmd += c
            else:
                cmd = c

            view.set_status(':{}'.format(cmd))

    hide_cursor()
    view.clear_status()

    return True

