# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from . import *
from .terminalsize import get_terminal_size

import time


def main():
    print("here we go")

    w,h = get_terminal_size()
    print("width = {}, height = {}".format(w,h))

    time.sleep(3)
    clear_screen()

    while True:
        c = read_char()
        i = ord(c)

        print("i got it: {} = {}".format(i, c))

        if i == 3: # ctrl c
            break

        elif i == 26: # ctrl z
            # TODO: ask to save changes
            break

