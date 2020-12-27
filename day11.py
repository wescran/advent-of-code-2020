#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from math import comb
def main():
    input_file = Path("inputs/day11.txt")
    with input_file.open("r") as f:
        # get all adapters
        data = [[ c for c in l.rstrip()] for l in f.readlines()]

    changes, e_count, o_count = 0, 0, 0
    while True:
        seats = [[] for i in range(len(data))]
        for i in range(len(data)):
            for j in range(len(data[i])):
                seat = data[i][j]
                if seat == "L":
                    if check_empty_slopes(i,j,data):
                        seat = "#"
                        changes += 1
                        o_count += 1
                    else:
                        e_count += 1
                elif seat == "#":
                    if check_occupied_slopes(i,j,data):
                        seat = "L"
                        changes += 1
                        e_count += 1
                    else:
                        o_count += 1
                seats[i].append(seat)
        if changes == 0:
            for line in data:
                print(''.join(line))
            break
        e_count, o_count, changes = 0,0,0
        data = seats
    print(o_count)
    print(sum(1 for i in range(len(seats)) for j in range(len(seats[i])) if seats[i][j] == "#"))

def check_empty_slopes(i,j,data):
    dirs = {"N": (-1,0), "NE": (-1,1), "E": (0,1), "SE": (1,1), "S": (1,0), "SW": (1,-1), "W": (0,-1), "NW": (-1,-1)}
    for d in dirs:
        di, dj = dirs[d]
        r,c = i + di, j + dj
        while 0<=r<len(data) and 0<=c<len(data[r]):
            if data[r][c] == "L":
                break
            elif data[r][c] == "#":
                return False
            r,c = r + di, c + dj
    return True

def check_occupied_slopes(i,j,data):
    dirs = {"N": (-1,0), "NE": (-1,1), "E": (0,1), "SE": (1,1), "S": (1,0), "SW": (1,-1), "W": (0,-1), "NW": (-1,-1)}
    count = 0
    for d in dirs:
        di, dj = dirs[d]
        r,c = i + di, j + dj
        while 0<=r<len(data) and 0<=c<len(data[r]):
            if data[r][c] == "#":
                count += 1
                if count >= 5:
                    return True
                break
            elif data[r][c] == "L":
                break
            r,c = r + di, c + dj
    return False

def check_empty(i,j,data):
    for a in range(i-1,i+2):
        for b in range(j-1,j+2):
            if 0<=a<len(data) and 0<=b<len(data[a]):
                if data[a][b] != "#":
                    continue
                else:
                    return False
    return True

def check_occupied(i,j,data):
    count = 0
    for a in range(i-1,i+2):
        for b in range(j-1,j+2):
            if 0<=a<len(data) and 0<=b<len(data[a]) and data[a][b] == "#" and (a,b) != (i,j):
                count += 1
                if count >= 4:
                    return True
    return False

main()
