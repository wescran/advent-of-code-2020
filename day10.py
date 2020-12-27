#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from math import comb
def main():
    input_file = Path("inputs/day10.txt")
    with input_file.open("r") as f:
        # get all adapters
        data = [int(l.rstrip()) for l in f]

    data.insert(0,0)
    jolts = 0
    diffs = defaultdict(int)
    adaps = sorted(data)
    adaps.append(adaps[-1] + 3)
    for adap in adaps:
        diff = adap - jolts
        diffs[diff] += 1
        jolts = adap
    print(diffs[1] * diffs[3])
    seen = {}
    seen[0] = 1
    for adap in adaps[1:]:
        seen[adap] = seen.get(adap-1,0) + seen.get(adap-2,0) + seen.get(adap-3,0)

    print(seen[max(adaps)])

main()
