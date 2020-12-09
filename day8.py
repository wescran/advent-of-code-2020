#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import re
def main():
    input_file = Path("inputs/day8.txt")
    switch = {}
    boot = []
    with input_file.open("r") as f:
        for n, line in enumerate(f):
            cmd,arg = line.rstrip().split(" ")
            boot.append((cmd,arg))
            if cmd in ["jmp","nop"]:
                switch[n] = cmd

    # part 1
    res = run(boot)
    print(res[0])

    # part 2
    for s in switch:
        p = switch[s]
        c = "jmp" if p == "nop" else "nop"
        cmd,arg = boot[s]
        boot[s] = (c,arg)
        res = run(boot)
        boot[s] = (cmd,arg)
        if res[1]:
            print(res[0])


def run(boot):
    i,acc = 0,0
    seen = set()
    while i not in seen:
        if i == len(boot):
            return(acc, True)
            break
        cmd, arg = boot[i]
        seen.add(i)
        if cmd == "acc":
            acc += int(arg)
        elif cmd == "jmp":
            i += int(arg)
            continue
        i += 1
    return(acc, False)

main()
