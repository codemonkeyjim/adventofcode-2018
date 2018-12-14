#!/usr/bin/env python


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
            opposite = curr.upper() if curr.islower() else curr.lower()
            if opposite == polymer[i+1]:
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
    for line in data:
        result = react(line)
        print(f'{len(result)}: {result}')
