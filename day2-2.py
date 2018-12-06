#!/usr/bin/env python

from itertools import permutations


def same_letters(a: str, b: str) -> str:
    match = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            match += a[i]
    return match


with open('data/day2.txt') as data:
    ids = data.read().splitlines()

max_pair = max(permutations(ids, 2), key=lambda pair: len(same_letters(*pair)))
print(max_pair)
print(same_letters(*max_pair))
