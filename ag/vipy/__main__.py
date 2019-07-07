# Copyright (C) 2019 Alpha Griffin
# @%@~LICENSE~@%@

def usage():
    print()
    print("Usage: vipy [options] [filename]")
    print()
    print("Where [options] are:")
    print("   -h  or  --help    Display this usage screen and exit")
    print("   --version         Print version information and exit")
    print()

from sys import argv, exit

filename = None

if len(argv) > 1:
    if argv[1][0] == '-':
        option = argv[1]

        if option == '-h' or option == '--help':
            usage()
            exit(0)

        elif option == '--version':
            from . import __version__
            print("vipy version {} by Alpha Griffin".format(__version__))
            exit(0)

        else:
            print("vipy: unknown option: {}".format(option))
            exit(1)

    else:
        filename = argv[1]

from .editor import main
main()

