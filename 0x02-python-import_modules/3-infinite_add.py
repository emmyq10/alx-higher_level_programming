#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    for arg in range(len(sys.argv) - 1):
        total += int(sys.argv[arg + 1])
    print("{}".format(total))
