# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

"""A vim-like editor in Python.

A Python module providing an interactive text-mode editor
that (partially) mimics the vim editor.

.. module:: ag.vipy
   :platform: Unix
   :synopsis: A vim-like editor in Python
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""

from .__version__ import __version__
from .buffer import MemoryBuffer
from .viewer import TerminalView
from .hotmode import read_action


def run(filename=None):
    print("vipy v{} startup".format(__version__))

    buf = MemoryBuffer()
    view = TerminalView()

    # load file into buffer, if specified
    if filename:
        buf.load(filename)
        view.fill(buf)

    view.refresh()

    while read_action(view):
        pass

    view.close()

