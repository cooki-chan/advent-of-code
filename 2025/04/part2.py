input = open('04/inp.txt').read().split('\n')

yMax = len(input)-1
xMax = len(input[0])-1

print(yMax, xMax)

rm = 0
itr = 0
while True:
    print(itr)
    rolls = []
    for y, i in enumerate(input):
        for x, j in enumerate(i):
            if j == "@":
                rolls.append(complex(y, x))

    o = []
    change = False

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
            o.append(i)
            rm +=1
            change = True
    
    for i in o:
        temp = list(input[int(i.real)])
        temp[int(i.imag)] = "."
        input[int(i.real)] = input[int(i.real)][0:int(i.imag)] + "." + input[int(i.real)][int(i.imag)+1:]

    if not change:
        break
    itr+=1


print(rm)