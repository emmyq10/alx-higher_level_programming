#!/usr/bin/python3

# import specific functions from calculator_1.py file
if__name__ == "__main__"
 """Print the sum, difference, multiple and quotient of 10 and 5."""
from calculator_1 import add, subtract, multiply, divide

# define variables a and b
a = 10
b = 5

# perform mathematical operations and print the results
sum_result = add(a, b)
diff_result = subtract(a, b)
product_result = multiply(a, b)
quotient_result = divide(a, b)

print("The sum of {} and {} is: {}".format(a, b, sum_result))
print("The difference between {} and {} is: {}".format(a, b, diff_result))
print("The product of {} and {} is: {}".format(a, b, product_result))
print("The quotient of {} divided by {} is: {}".format(a, b, quotient_result))
