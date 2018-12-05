#!/usr/bin/env python

from collections import Counter


with open('data/day2.txt') as data:
    twos = threes = 0
    for line in data.readlines():
        counts = Counter(line)
        twos += 2 in counts.values()
        threes += 3 in counts.values()
print(twos * threes)
