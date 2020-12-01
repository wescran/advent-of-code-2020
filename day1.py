#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

def main():
    input_file = Path("inputs/day1.txt")

    n_hash = defaultdict(int)
    with input_file.open("r") as f:
        for line in f:
            n_hash[int(line.rstrip("\n"))] += 1
    part1(n_hash)
    part2(n_hash)

def part1(n_hash):
    for number in n_hash:
        looking = 2020 - number
        if looking in n_hash:
            print(number * looking)
            return

def part2(n_hash):
    n_min = min(n_hash)
    for number1 in n_hash:
        for number2 in n_hash:
            number3 = 2020 - number1 - number2
            if number3 <= n_min:
                continue
            elif number3 in n_hash:
                print(number1 * number2 * number3)
                return
main()
