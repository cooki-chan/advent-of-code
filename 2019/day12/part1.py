input = open('day12/inp.txt').read().split('\n')

planets = []

# <x=2, y=-10, z=-7>
for i in input:
    raw = i.split(", ")
    planets.append([int(raw[0][3:]), int(raw[1][2:]), int(raw[2][2:-1])])

velo = [[0,0,0] for _ in range(4)]

for _ in range(2772):
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

eng = 0
for ind, i in enumerate(planets):
    eng += sum([abs(j) for j in i]) * sum([abs(k) for k in velo[ind]])

print(eng)
print(planets)
print(velo)



