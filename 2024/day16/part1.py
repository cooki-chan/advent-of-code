input = open('day16/inp.txt').read().split('\n')

tiles = set()
start = ()
end = ()

E = 1+0j
S = 0+1j
N = 0-1j
W  = -1+0j

for y, i in enumerate(input):
    for x, j in enumerate(i):
        match j:
            case ".":
                tiles.add(complex(x, y))
            case "E":
                end = complex(x,y)
            case "S":
                start = (complex(x,y), E, 0)
                tiles.add(complex(x, y))

searchers = [start]
record = []

def search(data):
    coord, direction, dist = data
    while(coord in tiles):
        
        cc = coord + (direction * 1j)
        if cc in tiles and cc not in record:
            searchers.append((cc, direction * 1j, dist + 1001))
            record.append(cc)

        c = coord + (direction * -1j)
        if c in tiles and c not in record:
            searchers.append((c, direction * -1j, dist + 1001))
            record.append(c)
        
        record.append(coord)
        coord += direction
        dist+=1
        

    record.append(coord)

    if coord == end:
        return dist
    return False


while len(searchers) > 0 and not searchers[0][0] == end:
    print(len(searchers))
    d = search(searchers.pop(0))
    if d:
        print(d, "END")
        break

