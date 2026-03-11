input = open('09/inp.txt').read().split('\n')

input = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in input]

pairs = []
for i in input:
    for j in input[input.index(i)+1:]:
        pairs.append((i, j))

pairs.sort(key = lambda x: (abs(x[0][0]-x[1][0])+1) * (abs(x[0][1]-x[1][1])+1), reverse = True)

x = pairs[0]
print((abs(x[0][0]-x[1][0])+1) * (abs(x[0][1]-x[1][1])+1))