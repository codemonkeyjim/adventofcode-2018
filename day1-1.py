#!/usr/bin/env python

with open('data/day1.txt') as data:
    print(sum(map(int, data.readlines())))