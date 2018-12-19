#!/usr/bin/env python

import math


X = 0
Y = 1

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

interior_points = [point for point in points if point[X] > min_x and point[X] < max_x and point[Y] > min_y and point[Y] < max_y]

print(f'Interior points: {interior_points}')

point_counts = {str(point): 0 for point in points}

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        dists = {}
        for point in points:
            dist = abs(point[X] - x) + abs(point[Y] - y)
            if dist not in dists:
                dists[dist] = []
            dists[dist].append(point)
        min_dist = min(dists.keys())
        # print(f'Point ({x}, {y}): nearest to {[f"({p[X]}, {p[Y]})" for p in dists[min_dist]]}  at {min_dist}')
        if len(dists[min_dist]) == 1:
            point_counts[str(dists[min_dist][0])] += 1

print(f'Point counts: {point_counts}')

max_point = max(interior_points, key=lambda point: point_counts[str(point)])
print(f'{max_point}: {point_counts[str(max_point)]}')
