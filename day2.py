"""Advent of code 2017 Day 2"""
import itertools

with open('input2.txt', 'r') as inp:
    LINES = [[int(x) for x in l.split()] for l in inp]

ANS1 = sum(max(l) - min(l) for l in LINES)
print(ANS1)

ANS2 = sum(b//a for l in LINES
           for a, b in itertools.combinations(sorted(l), 2)
           if b % a == 0)
print(ANS2)
