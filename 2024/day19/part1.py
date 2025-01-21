import re

input = open('day19/inp.txt').read()

def part_1(rawdata):
    available, _, *needed = rawdata.splitlines()
    available = available.split(", ")
    test = re.compile("(" + "|".join(f"({a})" for a in available) + ")+")
    print(test.fullmatch(needed[0]))
    for need in needed:
        print(need)
        print(test.fullmatch(need))

    return str(sum(test.fullmatch(need) is not None for need in needed))


print(part_1(input))