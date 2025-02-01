from math import lcm, gcd

input = open('day12/inp.txt').read().split('\n')


planets = []

# <x=2, y=-10, z=-7>
for i in input:
    raw = i.split(", ")
    planets.append([int(raw[0][3:]), int(raw[1][2:]), int(raw[2][2:-1])])

backup = planets.copy()
velo = [[0,0,0] for _ in range(4)]
record = ["" for _ in range(3)]
factors = [-1 for _ in range(3)]
fac = 0

while True:
#for _ in range(100):
    rec = []
    for i in planets[0]:
        rec.append(str(i))
    for ind, i in enumerate(rec):
        record[ind] += i
    
    for ind, i in enumerate(record):
        if len(i) > 3 and factors[ind] == -1 and i[0:len(i)//2] == i[len(i)//2:]:
            factors[ind] = (fac+1)//2


    fac+=1
    for ri, curr in enumerate(planets):
        for pi, comp in enumerate(planets):
            if curr == comp:
                continue
            for i in range(3):
                if curr[i] > comp[i]:
                    velo[ri][i] -=1
                elif curr[i] < comp[i]:
                    velo[ri][i] +=1
        
    for i in range(len(planets)):
        planets[i] = [i + j for i, j in zip(planets[i], velo[i])]

    if -1 not in factors:
        break
    
    if fac % 1000 == 0:
        print(fac, factors)

print(lcm(*factors))