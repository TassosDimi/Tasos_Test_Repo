#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 23:12:47 2025

@author: tasos
"""

import numpy as np
import matplotlib.pyplot as plt

# Coefficients for the quadratic equation ax^2 + bx + c = 0
a = 1
b = -3
c = 2

# Solve the quadratic equation using the quadratic formula
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    roots = [root1, root2]
else:
    roots = []

# Create x values for plotting
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# Plot the quadratic curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Mark the roots on the graph if they exist
if roots:
    for root in roots:
        plt.plot(root, 0, 'ro')  # Red dot at the root
        plt.text(root, 0, f'({root:.2f}, 0)', fontsize=10, ha='right')

plt.title('Quadratic Equation Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# Display the graph
plt.show()

# Display the roots
print(f"Roots: {roots}")
