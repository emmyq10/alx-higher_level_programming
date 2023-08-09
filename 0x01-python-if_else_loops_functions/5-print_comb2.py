#!/usr/bin/python3
for numb in range(0, 100):
    print("{:02}".format(numb), end=", " if numb < 99 else "\n")
