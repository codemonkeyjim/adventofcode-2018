#!/usr/bin/env python

import math
import re


def react(chain: str) -> str:
    changed = True
    polymer = chain

    while changed:
        reduced = ''
        changed = False
        i = 0
        while i < len(polymer):
            curr = polymer[i]
            if i == len(polymer) - 1:
                reduced += curr
                break
            if curr.swapcase() == polymer[i+1]:
                changed = True
                i += 2
                continue
            reduced += curr
            i += 1
        polymer = reduced
    return reduced


# for example in ('aA', 'abBA', 'aabAAB', 'dabAcCaCBAcCcaDA'):
#     print(f'{example}: {react(example)}')

with open('data/day5.txt') as data:
    results = {}
    min_len = math.inf
    min_ltr = None
    line = data.readline()
    for ltr in range(ord('a'), ord('z') + 1):
        ltr = chr(ltr)
        results[ltr] = react(re.sub(ltr, '', line, flags=re.IGNORECASE))
        if len(results[ltr]) < min_len:
            min_len = len(results[ltr])
            min_ltr = ltr
    print(f'{min_len} ({min_ltr}): {results[min_ltr]}')
