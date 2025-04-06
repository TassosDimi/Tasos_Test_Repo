#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:51:38 2025
@author: Anastasios Dimitriou
Location: Athens
This piece of code uses the function define in 'quadraticFunc.py' python file to solve
quadratic equations. 
"""

import quadraticFunc

# Ask users to define the quadratic function in the form of ax² + bx + c = 0
# That means we need user provide values for the arguments a, b, and c
print("To solve the quadratic equation ax² + bx + c = 0, we first need to define a, b, and c.")
try:
    a = float(input("Please enter the first number (a != 0): "))
    b = float(input("Please enter the second number, b: "))
    c = float(input("Please enter the third number, c: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    sys.exit()
    
print(f"\nThe quadratic equation is: ({a}x²) + ({b}x) + ({c}) = 0")  # Present the intended equation back to the user for confirmation.

# Call function to solve the quadratic equation using the user defined arguments.
quadraticFunc.quadraticF(a, b, c)
