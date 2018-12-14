#!/usr/bin/env python

from collections import Counter, defaultdict
import arrow
import re


LINE_PARSE = re.compile('^\[([^\]]+)\] (.+)\n?$')
GUARD_PARSE = re.compile('^Guard #(\d+) begins')

entries = {}

with open('data/day4.txt') as data:
    for line in data:
        ts_str, entry = LINE_PARSE.match(line).groups()
        ts = arrow.get(ts_str, 'YYYY-MM-DD HH:mm')
        entries[ts] = entry

guard_id = None
start_time = None
sleep_times = defaultdict(Counter)

for ts in sorted(entries.keys()):
    entry = entries[ts]
    if GUARD_PARSE.match(entry):
        if start_time:
            sleep_times[guard_id].update([minute.time().minute for minute in arrow.Arrow.range('minute', start_time, start_time.ceil('hour'))])
        guard_id = GUARD_PARSE.match(entry).group(1)
        start_time = None
    elif 'falls asleep' == entry:
        # start_time is midnight if ts.hour is 23
        if ts.time().hour == 23:
            ts = ts.shift(hour=0, minute=0, days=1)
        start_time = ts
    elif 'wakes up' == entry:
        sleep_times[guard_id].update([minute.time().minute for minute in arrow.Arrow.range('minute', start_time, ts.shift(minutes=-1))])
        start_time = None
    else:
        print('Unparseable line ({ts}): {entry}')

max_guard_id = None
max_duration = 0
for guard_id in sleep_times.keys():
    duration = sum(sleep_times[guard_id].values())
    if duration > max_duration:
        max_duration = duration
        max_guard_id = guard_id
max_minute = max(sleep_times[max_guard_id], key=sleep_times[max_guard_id].get)
print(f'Guard #{max_guard_id}: minute {max_minute} duration {max_duration} (answer: {int(max_guard_id) * max_minute})')