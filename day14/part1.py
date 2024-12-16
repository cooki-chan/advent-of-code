input = open('day14/inp.txt').read().split('\n')

robot = []
for i in input:
    p = []
    v = []

    pS = i.split(" ")[0].split("=")[1]
    vS = i.split(" ")[1].split("=")[1]

    p = [int(j) for j in pS.split(",")]
    v = [int(j) for j in vS.split(",")]

    robot.append([p, v])
input = robot

xBound = 101
yBound = 103

# xBound = 11
# yBound = 7

sec = 100

out = []
for i in input:
    p = i[0]
    v = i[1]

    pxF = p[0] + (v[0] * sec)
    pxF = pxF % xBound

    pyF = p[1] + (v[1] * sec)
    pyF = pyF % yBound

    out.append([pxF, pyF])

print(out)

qTL = []
qTR = []
qBL = []
qBR = []

for i in out:
    print(i)
    if i[0] > (xBound//2):
        if i[1] > yBound//2:
            qBR.append(i)
        
        if i[1] < yBound//2:
            qTR.append(i)

    elif i[0] < (xBound//2):
        if i[1] > yBound//2:
            qBL.append(i)
        
        if i[1] < yBound//2:
            qTL.append(i)


print(len(qTL))
print(len(qTR))
print(len(qBL))
print(len(qBR))
print(len(qTL) * len(qTR) * len(qBL) * len(qBR))
