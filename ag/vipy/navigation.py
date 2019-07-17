# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@


def navigate(view, c):
    if c == 'h' or c == b'h':
        view.move_left()

    elif c == 'l' or c == b'l':
        view.move_right()

    elif c == 'k' or c == b'k':
        view.move_up()

    elif c == 'j' or c == b'j':
        view.move_down()

    elif c == '0' or c == b'0':
        view.cursor[1] = 0
        view.refresh()

    elif c == 'w' or c == b'w':
        #pos = next_word(view)
        #if pos:
        #    view.cur = pos
        pass

    else:
        return False

    return True

'''
def next_word(view):
    pos = view.cur

    if pos[1] >= len(view.buf):
        return None

    while pos[1] < len(view.buf):
        line = view.buf[pos[1]]
        width = view.get_print_width(line)

        if pos[0] >= width:

        c = view.buf[pos[1]][pos[0]]
        while pos[0] < width:
'''

