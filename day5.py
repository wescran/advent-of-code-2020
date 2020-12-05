#!/usr/bin/env python3
from pathlib import Path
def main():
    input_file = Path("inputs/day5.txt")
    max_id = 0
    seats = set()
    with input_file.open("r") as f:
        for line in f:
            bsp = line.rstrip()
            row_bsp = bsp[:7]
            col_bsp = bsp[7:]
            seat_id = (get_row(row_bsp) * 8) + get_col(col_bsp)
            if seat_id > max_id:
                max_id = seat_id
            seats.add(seat_id)
    # part 1
    print(max_id)
    # part 2
    for i in range(1024):
        if i not in seats and (i - 1 in seats and i + 1 in seats):
            print(i)

def get_row(code):
    start = 0
    end = 128
    for l in code:
        if l == 'F':
            end = (start + end) // 2
        elif l == 'B':
            start = (start + end) // 2
    return start

def get_col(code):
    start = 0
    end = 8
    for l in code:
        if l == 'L':
            end = (start + end) // 2
        elif l == 'R':
            start = (start + end) // 2
    return start
main()
