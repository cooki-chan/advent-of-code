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


# area, perim
areas = {}

for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j in areas:
            areas[j][0] += 1
        else:
            areas[j] = [1, 0]

        if (row-1 >= 0 and not input[row-1][col] == j) or (row-1 < 0):
            areas[j][1] += 1 
        if (row+1 < len(input) and not input[row+1][col] == j) or (row+1 >= len(input)):
            areas[j][1] += 1 
        
        if (col-1 >= 0 and not input[row][col-1] == j) or (col-1 < 0):
            areas[j][1] += 1 
        if (col+1 < len(input[0]) and not input[row][col+1] == j) or (col+1 >= len(input[0])):
            areas[j][1] += 1 

print(areas)

out = 0
for i in areas.values():
    out += i[0] * i[1]

print(out)