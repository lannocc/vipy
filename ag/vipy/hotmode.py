# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .commands import read_command
from .navigation import navigate
from .termio import read_char

import sys
import time


def read_action(view):
    c = read_char()
    oc = ord(c)

    #print("i got it: {} = {}".format(oc, c))

    if oc == 3: # ctrl c
        return False

    elif oc == 26: # ctrl z
        # TODO: ask to save changes
        return False

    elif c == ':' or c == b':':
        if not read_command():
            return False

    elif navigate(view, c):
        pass

    else:
        print('?????? {}'.format(oc))
        sys.stdout.flush()
        time.sleep(1)

    return True

