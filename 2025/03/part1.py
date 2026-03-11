input = open('03/inp.txt').read().split('\n')

out = 0

for i in input:
    digits = list(set(list(i)))
    digits.sort(reverse = True)
    
    l = []

    for j in digits:
        m = list(set(list(i[i.index(j)+1:])))
        m.sort(reverse=True)
        try:
            l.append(f"{j}{m[0]}")
        except IndexError:
            print("wtv")
        

    l = [int(k) for k in l]

    l.sort(reverse=True)
    out += l[0]
    print(l[0])

print(out)