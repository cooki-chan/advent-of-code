input = open('05/inp.txt').read().split('\n')

ranges = []
out = 0
for i in input:
    if "-" in i:
        ranges.append((int(i.split("-")[0]),  int(i.split("-")[1])))

ranges.sort()
out = []
while len(ranges) > 1:
    curr = ranges[0]
    next = ranges[1]
    while len(ranges) > 2 and next[0] <= curr[1]:
        curr = (curr[0], next[1] if next[1] >= curr[1] else curr[1])
        ranges.pop(1)
        next = ranges[1]
    out.append(curr)
    ranges.pop(0)

out.append(ranges[0])
o = 0
for i in out:
    o += (i[1] - i[0]) + 1

print(o)