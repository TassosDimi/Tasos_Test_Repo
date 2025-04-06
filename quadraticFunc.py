#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:46:14 2025
@author: Anastasios Dimitriou
Location: Athens
The objective of this piece of code is to create a function that can solve a quadratic
equation for all real number values.
"""
import math, sys

# Function's definition, which accepts three compulsory parameters a, b, and c to form a quadratic equation (ax² + bx + c = 0).
def quadraticF(a, b, c):
    
    # Check that parameter 'a' is not zero, so a quadratic equation of the form ax² + bx + c = 0 exists.
    # If a is zero, then mention it using a print() statement, and give the single solution. Then exit the program (important to).
    if a == 0:
        print("\n\nThis is not a quadratic equation. It has exactly one solution.")
        result1 = (-c/b)
        print("The solution of the equation is x =", result1)
        print("Bye!")
        sys.exit()
    
    D = math.pow(b, 2) - 4 * a * c  # This is the discriminant of the quadratic equation.
    
    print("\nFor your quadratic equation the discriminant is D=", D)
    print("Based on this discrimiant we will now proceed to calculate the solutions, if there are any.")
    
    # Find the solutions of the quadratic equation based on the value of the discriminant D.
    if D > 0:
        root1 = round((-b + math.sqrt(D))/ (2*a), 4)
        root2 = round((-b - math.sqrt(D))/ (2*a), 4)
        print(f"\nThe solutions of the equation are x1 = {root1} and x2 = {root2}")
    elif D == 0:
        root = round((-b)/(2*a), 4)
        print(f"\nThe equation has exactly one solution x = {root}")
    else:
        print("\nYour quadratic equation has not real solutions.")
        print("Thank you!")
