# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from . import *

def main():
    print("here we go")

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

