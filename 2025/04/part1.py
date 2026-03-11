input = open('04/inp.txt').read().split('\n')

yMax = len(input)-1
xMax = len(input[0])-1

print(yMax, xMax)

rolls = []

for y, i in enumerate(input):
    for x, j in enumerate(i):
        if j == "@":
            rolls.append(complex(y, x))

o = 0

for i in rolls:
    count = 0
    d = []
    for j in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            d.append(complex(j, k))
    d.remove(complex(0,0))

    for j in d:
        c = i + j
        if yMax < c.real or c.real < 0 or xMax < c.imag or c.imag < 0:
            continue

        if(input[int(c.real)][int(c.imag)] == "@"):
            count+=1

    if count < 4:
        o+=1
        #print(i, count)

print(o)