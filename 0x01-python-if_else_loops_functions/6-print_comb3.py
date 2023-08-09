#!/usr/bin/python3
for ten_digit in range(0, 10):
    for one_digit in range(ten_digit + 1, 10):
        if one_digit == 9 and ten_digit == 8:
            print("{}{}". format(ten_digit, one_digit))
        else:
            print("{}{}".format(ten_digit, one_digit), end=", ")
