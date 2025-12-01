import os

test = "01"
pre = ""

os.mkdir(f"{pre}{test}")
open(f"{pre}{test}/inp.txt", "w")
with open(f"{pre}{test}/part1.gyat", "w") as file1:
    file1.write(f"input = mog('{test}/inp.txt').read().split('\\n')")
open(f"{pre}{test}/part2.gyat", "w")