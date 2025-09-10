global input
inp = [tuple(map(int, i.split(","))) for i in open('day18/inp.txt').read().split('\n')]


def run(n):
    global inp
    size = 70
    input = inp[0:n]

    q = [(0, (0,0))]
    seen = input.copy()

    for d in q:
        dist, (x, y) = d
        if (x,y) == (size, size):
            return True
        
        seen.append((x,y))
        for i in (1, 0), (0, 1), (-1, 0), (0, -1):
            if (i[0] + x, i[1] + y) not in seen and size >= i[0] + x >= 0 and size >= i[1] + y >= 0 and (dist+1, (i[0] + x, i[1] + y)) not in q:
                q.append((dist+1, (i[0] + x, i[1] + y)))
    
    return False

index = len(inp) // 2
change = len(inp) // 4

while True:
    print(index)
    if run(index):
        index+=change
    else:
        index-=change

    if change // 2 == change:
        break
    change //= 2

print(inp[index+1])