#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
def main():
    input_file = Path("inputs/day12.txt")
    part1(input_file)
    part2(input_file)

def part1(input_file):
    x,y = 0,0
    dirs = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}
    right = {"N": "E", "E": "S", "S": "W", "W": "N"}
    left = {"N": "W", "W": "S", "S": "E", "E": "N"}
    face = "E"
    with input_file.open("r") as f:
        for line in f:
            pos = line.rstrip()[0]
            dist = int(line.rstrip()[1:])
            if pos in "LR":
                if pos == "L":
                    turn = left
                else:
                    turn = right
                for i in range(dist // 90):
                    face = turn[face]
            else:
                dx,dy = dirs[face] if pos == "F" else dirs[pos]
                x,y = x + (dx * dist), y + (dy * dist)
    print(abs(x) + abs(y))

def part2(input_file):
    x,y = 0,0
    wx,wy = 10,1
    dirs = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}
    with input_file.open("r") as f:
        for line in f:
            pos = line.rstrip()[0]
            dist = int(line.rstrip()[1:])
            if pos in "LR":
                if pos == "L":
                    mult = (-1,1)
                else:
                    mult = (1,-1)
                for i in range(dist // 90):
                    wx,wy = wy*mult[0], wx*mult[1]
            elif pos in "NESW":
                dwx,dwy = dirs[pos]
                wx,wy = wx + (dwx * dist), wy + (dwy * dist)
            else:
                x,y = x + (wx * dist), y + (wy * dist)
    print(abs(x) + abs(y))
main()
