#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 09:31:30 2025

@author: tasos
<<<<<<< HEAD
Location: Athens
=======
Location: British Council
>>>>>>> f22c467c6124559001b4be2a2228cd0778228838
"""

import shutil
import unicodedata

def visible_width(text):
    return sum(2 if unicodedata.east_asian_width(char) in 'WF' else 1 for char in text)

def center_text(text, width):
    padding = (width - visible_width(text)) // 2
    return ' ' * padding + text

# Get terminal width
terminal_width = shutil.get_terminal_size().columns

# Print centered title
print(center_text("Πυθαγόρειες Τριάδες", terminal_width))
print("Μια Πυθαγόρεια Τριάδα είναι τρεις ακέραιοι που ικανοποιούν την εξίσωση a² + b² = c²\n")
print(center_text("(m² − n², 2mn, m² + n²)", terminal_width))
print("Όπου:")
print("m > n > 0 (θετικοί ακέραιοι)")
print("m και n είναι πρώτοι μεταξύ τους (δεν έχουν κοινούς διαιρέτες πέρα από το 1)")
print("")

# Function to generate Pythagorean triples
def generate_pythagorean_triples(limit):
    triples = []
    for m in range(1, limit):
        for n in range(m + 1, limit // 2):
            a = n**2 - m**2
            b = 2 * n * m
            c = n**2 + m**2
            if c > limit:
                break
            triples.append([a, b, c])
    return triples

# Get limit from user
limit = int(input("Θέστε το μέγιστο μήκος υποτεινούσας για τον υπολογισμό Πυθαγόρειων τριάδων: "))
triples = generate_pythagorean_triples(limit)

print("Με βαση την υποτεινουσα μηκους", limit, "εχουμε βρει", len(triples), "πυθαγορειες τριαδες.")
print("\nΠυθαγόρειες Τριάδες:")
for triple in triples:
    a, b, c = triple  # ✅ Correct unpacking
    print(f"Η πρωτη καθετη πλευρα εχει μηκος a = {a}, η δευτερη b = {b}, και η υποτεινουσα c = {c}")
    
print("\n\nThank you!")
    
    
    
    