input = open('day12/inp.txt').read().split('\n')


for num, i in enumerate(input):
    input[num] = list(i)

def replace(replacement, row, col):
    input[row][col] = replacement

    if (row-1 >= 0 and input[row-1][col] == j):
        input[row-1][col] = replacement
        replace(replacement, row-1, col)
    if (row+1 < len(input) and input[row+1][col] == j):
        input[row+1][col] = replacement
        replace(replacement, row+1, col)
    
    if (col-1 >= 0 and input[row][col-1] == j):
        input[row][col-1] = replacement
        replace(replacement, row, col-1)
    if (col+1 < len(input[0]) and input[row][col+1] == j):
        input[row][col+1] = replacement
        replace(replacement, row, col+1)

index = 0
for row, i in enumerate(input):
    for col, j in enumerate(i):
        if not type(j) == int:
            replace(index, row, col)
            index+=1


# area, sides
areas = {}

for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j in areas:
            areas[j][0] += 1
        else:
            areas[j] = [1, 0]

def rotate(arr):
    out = []
    for j in range(len(arr)):
        out.append([])

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            out[j].append(arr[i][j])
    
    for num in range(len(out)):
        out[num] = list(reversed(out[num]))
    return out

def priArr():
    for i in input:
        row = ""
        for j in i:
            row += str(j)
        print(row)

for i in areas.keys():
#for i in [0]:
    corners = 0
    for _ in range(4):
        for row, j in enumerate(input):
            for col, k in enumerate(j):
                if k == i:
                    if (row-1<0 or not input[row-1][col] == i) and (col-1<0 or not input[row][col-1] == i):
                        corners+=1
                    elif (not row-1<0 and input[row-1][col] == i) and (not col-1<0 and not input[row][col-1] == i) and input[row-1][col-1] == i:
                        corners +=1
        input = rotate(input)
    areas[i][1] += corners

out = 0
for i in areas.values():
    out += i[0] * i[1]

print(out)