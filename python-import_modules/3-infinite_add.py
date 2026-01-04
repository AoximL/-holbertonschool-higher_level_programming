#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total = 0

    i = 1
    while i < len(argv):
        total += int(argv[i])
        i += 1

    print(total)
