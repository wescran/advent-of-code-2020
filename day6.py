#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
def main():
    input_file = Path("inputs/day6.txt")
    group = defaultdict(int)
    a_count = 0
    b_count = 0
    g_count = 0
    with input_file.open("r") as f:
        for line in f:
            res = line.rstrip()
            if not res:
                a_count += len(group)
                b_count += sum(1 for c in group if group[c] == g_count)
                group = defaultdict(int)
                g_count = 0
                continue
            for q in res:
                group[q] += 1
            g_count += 1
    if group:
        a_count += len(group)
        b_count += sum(1 for c in group if group[c] == g_count)
    print(a_count,b_count)
main()
