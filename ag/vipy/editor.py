# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from . import *
from .terminalsize import get_terminal_size

import cursor
from termcolor import cprint

import time
import sys

def main(filename=None):
    print("vipy startup")
    cursor.hide()

    # viewport width and height
    vw,vh = get_terminal_size()
    print("width = {}, height = {}".format(vw,vh))

    # all text is buffered to memory
    buf = []

    # current displayed buffer line (top of viewport)
    line = 0

    # current cursor position in viewport (x,y)
    cur = [0, 0]

    # load file into buffer, if specified
    if filename:
        print("reading file: {}".format(filename))
        with open(filename, 'r') as f:
            buf = f.readlines()

    # FIXME: debug
    #time.sleep(1)


    def redraw():
        clear_screen()
        pos = [line, 0]

        for vrow in range(vh - 1):
            if pos[0] >= len(buf):
                break

            for vcol in range(vw):
                pos[1] += 1

                if pos[1] >= len(buf[pos[0]]):
                    pos[0] += 1
                    pos[1] = -1
                    print()
                    break

                c = buf[pos[0]][pos[1]]

                if c == '\r' or c == '\n':
                    continue

                if cur[0] == vcol and cur[1] == vrow:
                    #c = '\033[7m' + c + '\033[m'
                    cprint(c, attrs=["reverse"], end='')
                else:
                    print(c, end='')

        sys.stdout.flush()

    def read_command():
        print(':', end='')
        cursor.show()
        sys.stdout.flush()

        cmd = ''

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
                if len(cmd) > 0:
                    cmd = cmd[:-1]
                    print(c, end='') # FIXME: doesn't work (delete the character)
                    sys.stdout.flush()

            elif c == '\r' or c == '\n':
                if len(cmd) > 0:
                    if cmd == 'q' or cmd == 'q!':
                        return False

                break

            else:
                #print(oc)
                print(c, end='')
                sys.stdout.flush()
                cmd += c

        cursor.hide()
        return True


    while True:
        redraw()
        c = read_char()
        oc = ord(c)

        #print("i got it: {} = {}".format(oc, c))

        if oc == 3: # ctrl c
            break

        elif oc == 26: # ctrl z
            # TODO: ask to save changes
            break

        elif c == 'h':
            if cur[0] > 0:
                cur[0] -= 1

        elif c == 'l':
            if cur[0] < vw - 1:
                cur[0] += 1

        elif c == 'k':
            if cur[1] > 0:
                cur[1] -= 1

        elif c == 'j':
            if cur[1] < vh - 1:
                cur[1] += 1

        elif c == ':':
            quit = not read_command()
            if quit:
                break

        else:
            print(oc)
            sys.stdout.flush()

    cursor.show()

