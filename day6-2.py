#!/usr/bin/env python

import math


X = 0
Y = 1

LIMIT = 10000

points = []

with open('data/day6.txt') as data:
    for line in data:
        point = line.split(',')
        points.append(list(map(int, point)))

min_x = min_y = math.inf
max_x = max_y = -math.inf

for point in points:
    min_x = min(point[X], min_x)
    min_y = min(point[Y], min_y)
    max_x = max(point[X], max_x)
    max_y = max(point[Y], max_y)

print(f'Bounding box: ({min_x}, {min_y}):({max_x}, {max_y})')

safe_count = 0

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        dist = sum([abs(point[X] - x) + abs(point[Y] - y) for point in points])
        if dist < LIMIT:
            safe_count += 1

print(safe_count)
