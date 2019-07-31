# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@


class Presentable():

    def __init__(self, index, c):
        self.index = index  # position of character in buffer
        self.c = c          # real character
        self.continuation = False

