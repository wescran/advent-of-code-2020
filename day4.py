#!/usr/bin/env python3
from pathlib import Path
import re
def main():
    input_file = Path("inputs/day4.txt")
    valid = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    check = set()
    passport = {}
    a_count = 0
    b_count = 0
    invalid = False
    with input_file.open("r") as f:
        for line in f:
            for kv in line.rstrip().split(" "):
                try:
                    key, val = tuple(kv.split(":"))
                except ValueError:
                    if len(valid) == 0:
                        if not invalid:
                            b_count += 1
                        a_count += 1
                    valid = check | valid
                    check = set()
                    passport = {}
                    invalid = False
                    break
                if not invalid and not check_val(key,val):
                    invalid = True
                passport[key] = val
                if key in valid:
                    valid.remove(key)
                    check.add(key)
    if passport and len(valid) == 0:
        if not invalid:
            b_count += 1
        a_count += 1

    print(a_count, b_count)

def check_val(k,v):
    if k == "byr" and len(v) == 4 and (1920 <= int(v) <= 2002):
        return True
    elif k == "iyr" and len(v) == 4 and (2010 <= int(v) <= 2020):
        return True
    elif k == "eyr" and len(v) == 4 and (2020 <= int(v) <= 2030):
        return True
    elif k == "hgt":
        hgtp = re.compile("^(\d*)(cm|in)$")
        hgtm = hgtp.match(v)
        if hgtm and hgtm.group(2) == "cm" and (150 <= int(hgtm.group(1)) <= 193):
            return True
        elif hgtm and hgtm.group(2) == "in" and (59 <= int(hgtm.group(1)) <= 76):
            return True
    elif k == "hcl":
        hclp = re.compile("^#[0-9a-f]{6}$")
        if hclp.match(v):
            return True
    elif k == "ecl" and v in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return True
    elif k == "pid" and len(v) == 9:
        return True
    elif k == "cid":
        return True
    return False


main()
