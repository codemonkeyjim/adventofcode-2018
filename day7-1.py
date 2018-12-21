#!/usr/bin/env python

from collections import defaultdict

# Indexes into strings like "Step C must be finished before step A can begin."
STEP_IDX = 36
PREREQ_IDX = 5

prereqs = defaultdict(lambda: set())
all_steps = set()

with open('data/day7.txt') as steps:
    for line in steps:
        step = line[STEP_IDX]
        prereq = line[PREREQ_IDX]
        prereqs[step].add(prereq)
        all_steps.add(step)
        all_steps.add(prereq)

order = ''
no_prereqs = all_steps - set([step for step in prereqs.keys() if len(prereqs[step])])
while all_steps:
    current = min(no_prereqs)
    no_prereqs.remove(current)
    order += current
    for step in all_steps:
        if step == current:
            continue
        if current in prereqs[step]:
            prereqs[step].remove(current)
        if not prereqs[step]:
            no_prereqs.add(step)
    all_steps.remove(current)

print(order)
