input = open('06/inp.txt').read().split('\n')
parsed = []

for j in input:
    if not "*" in j:
        parsed.append([i for i in j.split(" ") if not i == ""])

eq = []
for i in range(len(parsed[0])):
    eq.append((parsed[4][i], int(parsed[0][i]),int(parsed[1][i]),int(parsed[2][i]), int(parsed[3][i])))

out = 0
for i in eq:
    print(i)
    if i[0] == "*":
        out += i[1] * i[2] * i[3]* i[4]
    else:
        out += i[1] + i[2] + i[3]+ i[4]

print(out)
