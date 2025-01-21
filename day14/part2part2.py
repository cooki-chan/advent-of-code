import time

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
sec = 1
while True:
    
    print(sec)

    out = []
    for i in input:
        p = i[0]
        v = i[1]

        pxF = p[0] + (v[0] * sec)
        pxF = pxF % xBound

        pyF = p[1] + (v[1] * sec)
        pyF = pyF % yBound

        out.append([pxF, pyF])
    
    sec+=1
    if len(set([tuple(i) for i in out])) == len(out):
        for i in range(yBound):
            prin = ""
            for j in range(xBound):
                if [i, j] in out:
                    prin+="*"
                else:
                    prin+=" "
            print(prin)
        
        print("__________________________________________________________________________________")
        break

print(out)