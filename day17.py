#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from copy import copy
def main():
    input_file = Path("inputs/day17.txt")
    initial_cube = {}
    with input_file.open() as f:
        for y, line in enumerate(f):
            ymax = y
            for x, val in enumerate(line.rstrip()):
                initial_cube[(x,y)] = val
                xmax = x
    part1(initial_cube,xmax, ymax)
    part2(initial_cube,xmax,ymax)

def part1(initial_cube,xmax,ymax):
    levels = {}
    levels[0] = defaultdict(level_factory)
    levels[0].update(initial_cube)
    levels[-1] = defaultdict(level_factory)
    levels[1] = defaultdict(level_factory)

    xmin,ymin = 0,0

    for cycle in range(6):
        new_levels = {}
        xmin -= 1
        ymin -= 1
        xmax += 1
        ymax += 1
        for level, cube in levels.items():
            new_level = defaultdict(level_factory)
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    new_level[(x,y)] = new_val(x, y, level, cube, levels)
            new_levels[level] = new_level
        levels = new_levels
        levels[min(levels) - 1] = defaultdict(level_factory)
        levels[max(levels) + 1] = defaultdict(level_factory)

    print(sum(1 for cube in levels.values() for val in cube.values() if val == "#"))

def part2(initial_cube,xmax,ymax):
    levels = {}
    for z in (0,-1,1):
        for w in (0,-1,1):
            levels[(z,w)] = defaultdict(level_factory)
    levels[(0,0)].update(initial_cube)

    xmin,ymin = 0,0

    for cycle in range(6):
        new_levels = {}
        xmin -= 1
        ymin -= 1
        xmax += 1
        ymax += 1
        for (z,w), cube in levels.items():
            new_level = defaultdict(level_factory)
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    new_level[(x,y)] = new_val_2(x, y, (z,w), cube, levels)
            new_levels[(z,w)] = new_level
        levels = new_levels
        zmin,wmin = min(levels)
        zmax,wmax = max(levels)
        for i in range(zmin-1,zmax+2):
            for j in range(wmin-1, wmax+2):
                try:
                    levels[(i,j)]
                except KeyError:
                    levels[(i,j)] = defaultdict(level_factory)
        if cycle == 1:
            print(zmin,wmin)
            print(zmax,wmax)
            for lv, cb in sorted(levels.items()):
                print(lv)
                for i in range(ymin, ymax+1):
                   print(*(cb[(j,i)] for j in range(xmin, xmax+1)))
                print()

    print(sum(1 for cube in levels.values() for val in cube.values() if val == "#"))
def new_val(x, y, lev, cube, levels):
    a_count = 0
    for z in (0,1,-1):
        try:
            lv = levels[lev + z]
        except KeyError:
            continue
        for i in (-1,0,1):
            for j in (-1,0,1):
                dx = x + i
                dy = y + j
                if z == 0 and ((dx,dy) == (x,y)):
                    continue
                elif lv[(dx,dy)] == "#":
                    a_count += 1
                    if a_count > 3:
                        return "."
    if cube[(x,y)] == "#" and (a_count == 2 or a_count == 3):
        return "#"
    elif cube[(x,y)] == "." and a_count == 3:
        return "#"
    return "."

def new_val_2(x,y,lev,cube,levels):
    a_count = 0
    z,w = lev
    for (dz,dw) in ((0,0),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1)):
        dz,dw = z + dz, w + dw
        try:
            level = levels[(dz,dw)]
        except KeyError:
            continue
        for i in (-1,0,1):
            for j in (-1,0,1):
                dx = x + i
                dy = y + j
                if (dz,dw) == (z,w) and ((dx,dy) == (x,y)):
                    continue
                elif level[(dx,dy)] == "#":
                    a_count += 1
                    if a_count > 3:
                        return "."
    if cube[(x,y)] == "#" and (a_count == 2 or a_count == 3):
        return "#"
    elif cube[(x,y)] == "." and a_count == 3:
        return "#"
    return "."

def level_factory():
    return "."
main()
