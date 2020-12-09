#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import re
def main():
    input_file = Path("inputs/day7.txt")
    contains = defaultdict(dict)
    inside = defaultdict(list)
    seen = set()
    with input_file.open("r") as f:
        for line in f:
            res = line.rstrip()
            pat_out = re.compile("^\w+\s\w+")
            pat_in = re.compile("(\d)\s(\w+\s\w+)")
            m_out = pat_out.match(res)
            m_in = pat_in.findall(res)
            for bag in m_in:
                inside[bag[1]].append(m_out.group())
                contains[m_out.group()][bag[1]] = bag[0]
    get_bags(inside,"shiny gold", seen)
    print(len(seen))
    count = get_count(contains,"shiny gold")
    print(count)
def get_bags(bags, key, seen):
    if bags[key] == []:
        return
    for bag in bags[key]:
        get_bags(bags, bag, seen)
        if bag not in seen:
            seen.add(bag)

def get_count(bags, key):
    if bags[key] == None:
        return 0
    count = 0
    for bag, n in bags[key].items():
        count += (get_count(bags, bag) * int(n)) + int(n)
    return count


main()
