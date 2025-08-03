# https://github.com/betyledix/lab10-BL
# Partner 1: Bety Ledix
# Partner 2:
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    """Calculate the square root of a"""
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Input must be a number")

def hypotenuse(a, b):
    """Calculate the hypotenuse of a right triangle with sides a and b"""
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Inputs must be numbers")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b