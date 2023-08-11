#!/usr/bin/python3

from calculator_1 import add, subtraction, multiply, divide

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, subtraction(a, b)))
print("{} * {} = {}".format(a, b, multiply(a, b)))
print("{} / {} = {}".format(a, b, divide(a, b)))
