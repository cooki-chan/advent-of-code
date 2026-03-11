input = open('12/inp.txt').read().split('\n\n')

gifts = []
for g in input:
    if ':' in g:
        n = []
        for row, i in enumerate(g.split('\n')[1:]):
            for col, j in enumerate(i):
                if j == '#':
                    n.append((row, col))
        gifts.append(n)

grids = []
for i in input[-1].split('\n'):
    n = []
    i = i.split(": ")
    
    dims = [int(j) for j in i[0].split('x')]
    needs = [int(j) for j in i[1].split(' ')]

    grids.append([dims, needs])

print(grids[0])

def find_fitting_spot(dims, filled, box):
    for row in range(dims[0]):
        for col in range(dims[1]):
            if (row, col) in filled:
                continue
            if box[0] + row <= dims[0] and box[1] + col <= dims[1]:
                return (row, col)
    return (-1, -1)

def pgrid(dims, filled):
    for row in range(dims[0]):
        out = ""
        for col in range(dims[1]):
            
            if (row, col) in filled.keys():
                out += str(filled[(row, col)])
            else:
                out += "."
        print(out)

test = 2
good = 0
for g in grids:
    special = [[(0,4), (1,1), (3,5)],
                [[3], [2], [3,4]],
                [[4], [2], [3,5]],
                [[1], [2], [4,4]],
                [[2], [2], [4,4]],]

    needs = g[1]
    dims = g[0]
    dims.sort()
    filled = {}
    success = True

    for _, spe in enumerate(special):
        print(spe)
        while True:
            exit = False
            for ind, i in enumerate(spe[0]):
                if needs[i] < spe[1][ind]:
                    exit = True
            if exit:
                break

            coords = find_fitting_spot(dims, filled, spe[2])
            if coords[0] == -1:
                break

            out = [(row, col, _) for row in range(coords[0], coords[0] + spe[2][0]) for col in range(coords[1], coords[1] + spe[2][1])]
            for i in out:
                filled[(i[0], i[1])] = i[2]
            for ind, i in enumerate(spe[0]):
                needs[i] -= spe[1][ind]

    print(needs)

    pgrid(dims, filled)
    
    for i in range(sum(needs)):
        coords = find_fitting_spot(dims, filled, (3,3))
        if coords[0] == -1:
            print("FAILED HAHA", sum(needs) - i, sum(needs))
            success = False
            break

        out = [filled.update({(row, col):9}) for row in range(coords[0], coords[0] + 3) for col in range(coords[1], coords[1] + 3)]
    
    pgrid(dims, filled)
    
    if success:
        good +=1
print(good)

