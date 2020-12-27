#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from itertools import count
def main():
    input_file = Path("inputs/day16.txt")
    ranges = set()
    cols = {}
    with input_file.open() as f:
        # get field ranges
        line = f.readline().rstrip()
        while line != "":
            col_name, fields = line.split(":")
            a_start, a_end = (int(i) for i in fields.split(" ")[-3].split("-"))
            b_start, b_end = (int(i) for i in fields.split(" ")[-1].split("-"))

            cols[col_name] = (range(a_start,a_end+1), range(b_start,b_end+1))

            set_a = set(i for i in range(a_start, a_end + 1))
            set_b = set(i for i in range(b_start, b_end + 1))
            ranges = ranges | set_a | set_b
            line = f.readline().rstrip()

        # get your ticket
        line = f.readline()
        your = [int(i) for i in f.readline().rstrip().split(",")]
        line = f.readline()
        line = f.readline()

        # get nearby tickets
        nearby = [line.rstrip().split(",") for line in f]

        valid = part1(ranges, nearby)
        print(len(valid), len(nearby))

        part2(cols, valid, your)

def part1(ranges, nearby):
    error = 0
    valid = []
    for ticket in nearby:
        found = False
        for num in ticket:
            n = int(num)
            if n not in ranges:
                error += n
                found = True
        if not found:
            valid.append(ticket)
    print(error)
    return valid

def part2(cols, valid, your):
    names = {}
    for i in range(len(valid[0])):
        ranges = dict(cols)
        for ticket in valid:
            val = int(ticket[i])
            reduced = dict(ranges)
            for col,(rng_a, rng_b) in ranges.items():
                set_a = set(i for i in rng_a)
                set_b = set(i for i in rng_b)
                if val not in (set_a | set_b):
                    reduced.pop(col)
            ranges = dict(reduced)
        names[i] = ranges

    set_names = set()
    heads = {}
    for col in sorted(names, key=lambda x: len(names[x])):
        ranges = names[col]
        if len(ranges) != 1:
            for name in set_names:
                ranges.pop(name)
        name = next(iter(ranges))
        set_names.add(name)
        heads[col] = name


    res = 1
    for col, val in zip(sorted(heads),your):
        if "departure" in heads[col]:
            res *= int(val)
    print(res)

main()
