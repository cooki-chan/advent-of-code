input = open('05/inp.txt').read().split('\n')

ranges = []

s = []
for i in input:
    if "-" in i:
        s.append((int(i.split("-")[0]), int(i.split("-")[1])))

out = 0
for i in input:
    if "-" not in i and not i == "":
        fr = False
        for j in s:
            if j[0] <= int(i) and j[1] >= int(i):
                fr = True
        if fr:
            out+=1

print(out)