# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .commands import read_command
from .typing import read_input
from .navigation import navigate
from .termio import read_char

import sys
import time


def read_action(view):
    c = read_char()
    oc = ord(c)

    if oc == 3: # ctrl c
        return False

    elif oc == 26: # ctrl z
        # TODO: ask to save changes
        return False

    elif c == ':' or c == b':':
        if not read_command(view):
            return False

    elif c == 'a' or c == b'a' or c == 'i' or c == b'i':
        if not read_input(view):
            return False

    elif navigate(view, c):
        pass

    else:
        status = view.status
        view.set_status('?????? {}'.format(oc))
        time.sleep(1)
        view.set_status(status)

    return True

