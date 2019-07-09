# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@


def navigate(view, c):
    if c == 'h' or c == b'h':
        if view.cur[0] > 0:
            view.cur[0] -= 1

    elif c == 'l' or c == b'l':
        if view.cur[0] < view.width - 1:
            view.cur[0] += 1

    elif c == 'k' or c == b'k':
        if view.cur[1] > 0:
            view.cur[1] -= 1

    elif c == 'j' or c == b'j':
        if view.cur[1] < view.height - 1:
            view.cur[1] += 1

    elif c == '0' or c == b'0':
        view.cur[0] = 0

    else:
        return False

    return True

