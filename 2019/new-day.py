import os

test = 11
pre = "./"

os.mkdir(f"{pre}day{test}")
open(f"{pre}day{test}/inp.txt", "w")
with open(f"{pre}day{test}/part1.py", "w") as file1:
    file1.write(f"input = open('day{test}/inp.txt').read().split('\\n')")
open(f"{pre}day{test}/part2.py", "w")

