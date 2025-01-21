input = open('day9/inp.txt').read()

disk = []

free = False
index = 0
for i in input:
    added = -1
    if not free:
        added = index
        index+=1
    free = not free
    
    for _ in range(int(i)):
        disk.append(added)

while -1 in disk:
    out = disk.pop()
    disk[disk.index(-1)] = out

out = 0
for ind, i in enumerate(disk):
    out += ind * i

print(out)