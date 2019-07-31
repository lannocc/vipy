# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

from .presenting import Presentable


class MemoryBuffer():

    def __init__(self):
        self.data = []

    def load(self, filename):
        print("reading file: {}".format(filename))

        with open(filename, 'r') as f:
            self.data = f.read()

    def __iter__(self):
        return self.presenting()

    def presenting(self, start=0):
        return self.Iterator(self, start)

    class Iterator():
        def __init__(self, buf, start=0):
            self.buf = buf
            self.index = start

        def __next__(self):
            if self.index >= len(self.buf.data):
                raise StopIteration

            p = self.buf.presentable(self.index)
            self.index += 1

            return p

    def handle_insert(self, view, s):
        pass

    def presentable(self, index):
        p = Presentable(index, self.data[index])
        return p

