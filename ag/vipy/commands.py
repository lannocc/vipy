# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .termio import read_char

import cursor

import sys


def read_command():
    print(':', end='')
    cursor.show()
    sys.stdout.flush()

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
            #print(c, end='') # FIXME: doesn't work (delete the character)
            print('\r:{} '.format(cmd), end='') # this blanks the previous character
            print('\r:{}'.format(cmd), end='') # this resets cursor position
            sys.stdout.flush()

        elif c == '\r' or c == b'\r' or c == '\n' or c == b'\n':
            if cmd and len(cmd) > 0:
                if cmd == 'q' or cmd == b'q' or cmd == 'q!' or cmd == b'q!':
                    return False

            break

        else:
            #print(oc)
            print(c, end='')
            sys.stdout.flush()

            if cmd:
                cmd += c
            else:
                cmd = c

    cursor.hide()
    return True


