#!/usr/bin/env python

from collections import Counter
import re

CLAIMS = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

claims = {}
fabric = Counter()

with open('data/day3.txt') as data:
    for claim in data.readlines():
        coords = re.match(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', claim)
        claim_id = coords.group('id')
        x = int(coords.group('x'))
        y = int(coords.group('y'))
        w = int(coords.group('w'))
        h = int(coords.group('h'))
        claims[claim_id] = []
        for i in range(x, x+w):
            for j in range(y, y+h):
                addr = f'{i},{j}'
                fabric.update([addr])
                claims[claim_id].append(addr)

print(sum(val > 1 for val in fabric.values()))

for claim_id, claim in claims.items():
    if all([fabric[claim_id] == 1 for claim_id in claim]):
        print(claim_id)
        break
