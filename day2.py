#!/usr/bin/env python3
from pathlib import Path
from collections import Counter

def main():
    input_file = Path("inputs/day2.txt")
    a_count, b_count = 0, 0
    with input_file.open("r") as f:
        for line in f:
            policy, letter, pword = tuple(line.rstrip("\n").split())
            c = Counter(pword)
            print(policy, letter, pword, c[letter[0]])
            pos_a = int(policy.split("-")[0])
            pos_b = int(policy.split("-")[-1])
            if (pos_a <= c[letter[0]] <= pos_b):
                a_count += 1
            if (pword[pos_a - 1] == letter[0] and pword[pos_b - 1] != letter[0]) or (pword[pos_a - 1] != letter[0] and pword[pos_b - 1] == letter[0]):
                b_count += 1
    print(a_count, b_count)

main()
