#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    _len = len(argv) - 1
    if _len == 0:
        print("0 arguments.")
    elif _len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(_len))

    for i in range(_len):
        print("{}: {}".format(i + 1, argv[i + 1]))
        i += 1
