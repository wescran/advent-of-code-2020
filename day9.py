#!/usr/bin/env python3
from pathlib import Path
def main():
    input_file = Path("inputs/day9.txt")
    preamble = []
    data = []
    with input_file.open("r") as f:
        # get preamble of 25 numbers
        for n, line in enumerate(f):
            preamble.append(int(line.rstrip()))
            if n == 24:
                break
        for line in f:
            num = int(line.rstrip())
            if not is_sum(num, preamble):
                print(num)
                weak = num
                #preamble.append(num)
                break
            data.append(preamble.pop(0))
            preamble.append(num)

        data.extend(preamble)
        #for line in f:
        #    data.append(int(line.rstrip()))

    cont = []
    for num in reversed(data):
        cont.append(num)
        print(cont)
        if len(cont) > 1 and sum(cont) == weak:
            print(cont, min(cont) + max(cont))
            break
        elif len(cont) > 1 and sum(cont) > weak:
            while len(cont) > 2 and sum(cont) > weak:
                cont.pop(0)
                print(cont)
            if len(cont) > 1 and sum(cont) == weak:
                print(cont, min(cont) + max(cont))
                break

def is_sum(n, numbers):
    for i in numbers:
        if j := n - i in numbers:
            return True
    return False

main()
