"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for itm in items:
        frequencies[str(itm)] = 1+frequencies.get(str(itm), 0)

    return frequencies
