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


import os
import sys

def _read_char():
    try:
        import termios

    except ImportError:
        # Non-POSIX; assume Windows
        import msvcrt
        return msvcrt.getch

    # POSIX
    import tty

    def getch():
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)

        return char

    return getch

read_char = _read_char()


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

