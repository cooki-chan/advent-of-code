input = open('03/inp.txt').read().split('\n')

out = 0
itr = 12

def bestPossible(str):
    l = list(str)
    l.sort()
    if len(l) < itr:
        return ""
    while len(l) > itr:
        l.pop(0)
    reb = ""
    for i in str[::-1]:
        print(l)
        if i in l:
            reb += i
            l.remove(i)
    return reb[::-1]


for i in input:
    h = list(set(list(i)))
    h.sort(reverse=True)

    temp = []
    for j in h:
        temp += [i.index(j)]
    h = temp

    t = bestPossible(i[h[0]:])
    while(t == ""):
        h.pop(0)
        t = bestPossible(i[h[0]:])
    out += int(t)
    print(int(t))

print(out)