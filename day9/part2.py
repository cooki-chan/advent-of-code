input = open('day9/inp.txt').read()

disk = []

free = False
index = 0
table = {}
for i in input:
    added = -1
    if not free:
        added = index
        index+=1
    free = not free

    if int(i) == 0:
        continue

    if int(i) > 0:
        disk.append((added, int(i)))
        table[added] = int(i)
    


for i in range(index-1, -1, -1):
    # print(disk)
    if not i in table.keys():
        continue
    indOf = disk.index((i, table[i]))
    valOf = disk[indOf]

    for i in range(indOf):
        if disk[i][0] == -1 and disk[i][1] >= valOf[1]:
            if disk[i][1] == valOf[1]:
                disk[i] = valOf
                temp = disk.pop(indOf)
                disk.insert(indOf, (-1, temp[1]))
                break
            
            elif disk[i][1] > valOf[1]:
                temp = disk.pop(indOf)
                disk.insert(indOf, (-1, temp[1]))
                disk.insert(i+1, (-1, disk[i][1] - valOf[1]))
                disk[i] = valOf
                break

    index = 0
    while not index == len(disk)-1:
        if disk[index][0] == -1 and disk[index+1][0] == -1:
            disk[index] = (-1, disk[index][1] + disk[index+1][1])
            disk.pop(index+1)
            index-=2
        index+=1
        

    # print(disk)
    # print()

out = []
for i in disk:
    for _ in range(i[1]):
        added = i[0]
        if i[0] == -1:
            added = 0
        out.append(added)

t = 0
for n, i in enumerate(out):
    t += i * n

print(t)