#!/usr/bin/env python

total = 0
totals = set()

while True:
    with open('data/day1.txt') as data:
        for val in map(int, data.readlines()):
            total += val
            if total in totals:
                print(total)
                exit()
            totals.add(total)
