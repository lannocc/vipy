####
vipy
####

A vim-like text-mode editor as a Python module.

CONTRIBUTIONS WELCOME: this is a work in progress.


*********
Why vipy?
*********

Necessity is the mother of invention. The developer was working remotely on a Windows machine through SSH that had Python installed, and needed an editor.


************
Requirements
************

Python 3.6 or higher. This "editor" should work on Linux, MacOS/BSD, and Windows.

**vipy is pure python and has no external dependencies**


**********
Installing
**********

Install through pip::

    python -m pip install git+https://github.com/lannocc/vipy


*****
Using
*****

Once installed, you can start a blank editor::

    vipy

Edit a new or existing file::

    vipy myfile.txt

See the help screen::

    vipy --help


Basics
======

vipy starts up in **hot mode**. This mode provides quick access to actions such as navigation, mode switching, and other commands.


Hot Mode
========

Hot mode is the default mode and you can always return to hot mode by pressing the 'Esc' (escape) key.

Navigation
----------

Simple screen cursor movement:

- **h** - move left
- **j** - move down
- **k** - move up
- **l** - move right


Typing Mode
===========

Typing mode is accessed through any number of actions:

- **i** - insert
- **a** - append


Command Mode
============

Command mode is accessed by pressing the ':' (colon) key from within hot mode. Return to hot mode by pressing the 'Esc' (escape) key.

Commands include:

- **q** - quit



**FIXME: More to come later.**

