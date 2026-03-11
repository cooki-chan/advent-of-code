import os

test = "12"
pre = "./"

os.mkdir(f"{pre}{test}")
open(f"{pre}{test}/inp.txt", "w")
with open(f"{pre}{test}/part1.py", "w") as file1:
    file1.write(f"input = open('{test}/inp.txt').read().split('\\n')")
open(f"{pre}{test}/part2.py", "w")

