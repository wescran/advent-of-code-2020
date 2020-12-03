#!/usr/bin/env python3
from pathlib import Path

def main():
    input_file = Path("inputs/day3.txt")
    with input_file.open("r") as f:
        land = [l.rstrip() for l in f.readlines()]

    # part 1
    print(get_trees(land, (1,3)))

    # part 2
    prod = 1
    for slope in [(1,1),(1,3),(1,5),(1,7),(2,1)]:
        prod *= get_trees(land, slope)

    print(prod)


def get_trees(land, slope):
    imax = len(land)
    jmax = len(land[0])
    y,x = slope
    i,j = y,x
    trees = 0
    while True:
        # at bottom
        if i >= imax:
            break
        # at right end
        if j >= jmax:
            j -= jmax
        if land[i][j] == '#':
            trees += 1

        i += y
        j += x
    return trees

main()
