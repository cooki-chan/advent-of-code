input = open('day25/inp.txt').read().split('\n\n')
input = [i.split("\n") for i in input]

locks = []
keys = []

temp = [-1,-1,-1,-1,-1]
for i in input:
    temp = [-1,-1,-1,-1,-1]
    if i[0] == "#####":
        for level, j in enumerate(i):
            for val, k in enumerate(j):
                if k == "." and temp[val] == -1:
                    temp[val] = level-1
        locks.append(temp)

    else:
        for level, j in enumerate(reversed(i)):
            for val, k in enumerate(j):
                if k == "." and temp[val] == -1:
                    temp[val] = level-1
        keys.append(temp)

out = 0
for i in locks:
    for j in keys:
        fail = False
        for v in range(5):
            if i[v] + j[v] > 5:
                fail = True
        if not fail:
            out+=1
            

print(out)
