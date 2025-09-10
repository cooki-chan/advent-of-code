input = open('day18/inp.txt').read().split('\n')

size = 70
n = 2908
input = [tuple(map(int, i.split(","))) for i in input][0:n]

q = [(0, (0,0))]
seen = input.copy()
out = -1

for d in q:
    print(d)
    dist, (x, y) = d
    if (x,y) == (size, size):
        print(dist)
        break
    
    seen.append((x,y))
    for i in (1, 0), (0, 1), (-1, 0), (0, -1):
        if (i[0] + x, i[1] + y) not in seen and size >= i[0] + x >= 0 and size >= i[1] + y >= 0 and (dist+1, (i[0] + x, i[1] + y)) not in q:
            q.append((dist+1, (i[0] + x, i[1] + y)))


