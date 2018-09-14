# Copyright (C) 2017-2018 Alpha Griffin
# @%@~LICENSE~@%@

"""Alpha Griffin Python Starter Project

The sample Alpha Griffin project allows you to easily get started
on a new Python project matching the Alpha Griffin development
conventions and standards.

.. module:: ag.pyproject
   :platform: Unix
   :synopsis: Python Starter Project for Alpha Griffin
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""

from .__version__ import __version__
print ("Sample Alpha Griffin Python project version %s" % (__version__))

import ag.logging as log
log.set(log.INFO)

