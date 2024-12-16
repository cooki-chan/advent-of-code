input = open('day12/inp.txt').read().split('\n')


for num, i in enumerate(input):
    input[num] = list(i)

# replaces letters that are connected into unique numbers
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

# area, edges
areas = {}

#calculate area
for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j in areas:
            areas[j][0] += 1
        else:
            areas[j] = [1, 0]

#rotates a 2d array 
def rotate(arr):
    out = []
    for j in range(len(arr)):
        out.append([])

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            out[j].append(arr[i][j])
    return out

#takes a list and a value, and returns a list with all other values replaced with -1
def clean(list, val):
    out = list.copy()
    for ind, i in enumerate(out):
        if not i == val:
            out[ind] = -1
    
    return out

#scans top to bottom and counts the number of edges as it goes down
def scan(val):
    edg = 0
    before = clean(input[0], val)
    innd = 0

    #Count number of edges if the top is at index 0
    if val in input[0]:
        innd=0
        inEdge = False
        for ind, j in enumerate(clean(input[innd], val)):
            if not -1 == j and not inEdge:
                inEdge = True
                edg+=1
                continue
            
            if -1 == j:
                inEdge = False

    #Count number of edges if the bottom is at the bottom of the 2d array
    if val in input[len(input)-1]:
        innd= len(input)-1

        inEdge = False
        for ind, j in enumerate(clean(input[innd], val)):
            if not -1 == j and not inEdge:
                inEdge = True
                edg+=1
                continue
            
            if -1 == j:
                inEdge = False

    #scanning logic
    for i in input:
        inEdge = False
        lastCombo = (-1, -1) #used for the case where the values switch
        for ind, j in enumerate(clean(i, val)):
            if (not before[ind] == j and not inEdge) or (before[ind] == lastCombo[1] and j == lastCombo[0] and not before[ind] == j):
                inEdge = True
                edg+=1
                
            
            elif before[ind] == j:
                inEdge = False
            lastCombo = (before[ind], j)
        before = clean(i, val)
    return edg

for i in areas.keys():
    areas[i][1] = 0

    areas[i][1] += scan(i)
    input = rotate(input)
    
    areas[i][1] += scan(i)
    input = rotate(input)

    input = rotate(input)
    input = rotate(input)

out = 0
for i in areas.values():
    out += i[0] * i[1]

print(out)