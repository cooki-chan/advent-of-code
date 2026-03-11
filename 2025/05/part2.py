input = open('05/inp.txt').read().split('\n')

ranges = []

out = 0
for i in input:
    if "-" in i:
        ranges.append((int(i.split("-")[0]),  int(i.split("-")[1])))

while(True):
    ranges.sort()
    change = False
    for i in ranges:
        print(ranges, i)
        br = False
        for j in ranges[ranges.index(i)+1:]:
            if i == j:
                continue
            if i[0] >= j[0] and i[1] <= j[1]:
                ranges.remove(i)
                br = True
                change = True
                break
            if i[0] <= j[0] and i[1] >= j[1]:
                ranges.remove(j)
                br = True
                change = True
                break
            
            if i[1] >= j[0] and i[0] <= j[1]:
                ranges.remove(i)
                ranges.remove(j)
                ranges.append((i[0], j[1]))
                br = True
                change = True
                break
            if i[0] <= j[1] and j[0] <= i[1]:
                ranges.remove(i)
                ranges.remove(j)
                ranges.append((j[0], i[1]))
                br = True
                change = True
                break
        if br:
            break
        
    if not change:
        break
            



out = 0
for i in ranges:
    out += (i[1] - i[0]) + 1

print(out)