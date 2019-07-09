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

from .viewer import View
from .hotmode import read_action
from .__version__ import __version__

import cursor


def run(filename=None):
    print("vipy {} startup".format(__version__))
    cursor.hide()

    view = View()

    # load file into buffer, if specified
    if filename:
        view.load(filename)

    # FIXME: debug
    #time.sleep(1)

    while True:
        view.draw()

        if not read_action(view):
            break

    cursor.show()

