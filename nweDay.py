import os
import datetime

test = 10



os.mkdir(f"day{test}")
open(f"day{test}/inp.txt", "w")
with open(f"day{test}/part1.py", "w") as file1:
    file1.write(f"input = open('day{test}/inp.txt').read().split('\n')")
    
open(f"day{test}/part2.py", "w")

