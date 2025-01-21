input = open('day10/inp.txt').read().split('\n')

map = []
for i in input:
    map.append(list(i))

def search(coord):
    out = 0
    valAt = int(map[coord[0]][coord[1]])


    if valAt == 9:
        return 1

    if coord[0]-1 > -1 and not map[coord[0]-1][coord[1]] == "." and int(map[coord[0]-1][coord[1]]) == valAt + 1:
        out+=search((coord[0]-1, coord[1]))

    if coord[0]+1 < len(map) and not map[coord[0]+1][coord[1]] == "." and  int(map[coord[0]+1][coord[1]]) == valAt + 1:
        out+=search((coord[0]+1, coord[1]))

    if   coord[1]-1 > -1 and not map[coord[0]][coord[1]-1] == "." and int(map[coord[0]][coord[1]-1]) == valAt + 1:
        out+=search((coord[0], coord[1]-1))

    if  coord[1]+1 < len(map[0]) and  not map[coord[0]][coord[1]+1] == "." and int(map[coord[0]][coord[1]+1]) == valAt + 1:
        out+=search((coord[0], coord[1]+1))
    
    return out

fullO = 0
for row, i in enumerate(map):
    for col, j in enumerate(i):
        if not j == "." and int(j) == 0:
            print((row, col))
            temp = search((row, col))
            fullO+=temp
            print(temp)

print(fullO)