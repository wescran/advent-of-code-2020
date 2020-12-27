#!/usr/bin/env python3
from pathlib import Path
from itertools import count
import re
def main():
    input_file = Path("inputs/day13.txt")
    with input_file.open("r") as f:
        timestamp = int(f.readline().rstrip())
        sched = f.readline().rstrip()

    pat = re.compile("\d+")
    matches = [int(m) for m in pat.findall(sched)]

    print(timestamp, matches)

    part1(timestamp, matches)
    part2(sched)

def part1(ts, buses):
    wait = {}
    for b in buses:
        mod = ts % b
        if mod == 0:
            print(0)
            return
        else:
            wait[b] = b - mod
    res = min(wait, key=lambda x: wait[x])
    print(res * wait[res])

def part2(buses):
    print(buses.split(","))
    times = {}
    cnt = 0
    for b in buses.split(","):
        try:
            times[int(b)] = cnt
            cnt += 1
        except ValueError:
            cnt += 1

    step = 1
    start = 100000000000000
    for b, cnt in times.items():
        for c in count(start,step):
            if (c + cnt) % b == 0:
                start = c
                break
        step *= b
    print(start)

main()
