import os

test = 9
pre = "C:/Users/ethan/Desktop/GADIG/advent-of-code-2024/"

os.mkdir(f"{pre}day{test}")
open(f"{pre}day{test}/inp.txt", "w")
with open(f"{pre}day{test}/part1.py", "w") as file1:
    file1.write(f"input = open('day{test}/inp.txt').read().split('\\n')")
open(f"{pre}day{test}/part2.py", "w")

