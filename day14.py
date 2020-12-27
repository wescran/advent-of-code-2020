#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from itertools import combinations
def main():
    input_file = Path("inputs/day14.txt")
    part1(input_file)
    part2(input_file)

def part1(input_file):
    mem = defaultdict(int)
    with input_file.open("r") as f:
        for line in f:
            inst = line.rstrip().split("=")
            cmd = inst[0].rstrip(" ")
            val = inst[1].strip(" ")
            if cmd == "mask":
                mask = val
            else:
                loc = cmd[4:-1]
                num = [c for c in f"{int(val):036b}"]
                for i, m in enumerate(mask):
                    if m == "0":
                        num[i] = "0"
                    elif m == "1":
                        num[i] = "1"
                mem[loc] = int("".join(num), 2)
    print(sum(mem.values()))

def part2(input_file):
    mem = defaultdict(int)
    with input_file.open("r") as f:
        for line in f:
            inst = line.rstrip().split("=")
            cmd = inst[0].rstrip(" ")
            val = inst[1].strip(" ")
            if cmd == "mask":
                mask = val
            else:
                loc = [c for c in f"{int(cmd[4:-1]):036b}"]
                xc = 0
                x_loc = []
                for i, m in enumerate(mask):
                    if m == "X":
                        loc[i] = "X"
                        x_loc.append(i)
                        xc += 1
                    elif m == "1":
                        loc[i] = "1"
                for bits in set(combinations('10'*xc, xc)):
                    for b, i in zip(bits, x_loc):
                        loc[i] = b
                    mem[int("".join(loc), 2)] = int(val)
    print(sum(mem.values()))

main()
