#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from itertools import count
def main():
    input_file = Path("inputs/day15.txt")
    turns = {}
    mem = {}
    number = defaultdict(int)
    initial = input_file.read_text().rstrip().split(",")
    counter = count(1)
    for num in initial:
        n = int(num)
        turn = next(counter)
        turns[turn] = n
        mem[n] = turn
        number[n] += 1

    turn = next(counter)
    print(turns, mem)
    while turn != 30000001:
        prev = turns[turn - 1]
        if number[prev] > 1:
            n = (turn-1) - mem[prev]
            mem[prev] = turn - 1
        else:
            n = 0
            mem[prev] = turn - 1
        turns[turn] = n
        number[n] += 1
        turn = next(counter)

    print(n)

main()
