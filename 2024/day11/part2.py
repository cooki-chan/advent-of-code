global b 
b = 0

def logic(i):
    global b
    b+=1
    if i == 0:
        return 1
    
    elif len(str(i)) % 2 == 0:
        lenn = 0
        tem = i
        while tem > 0:
            lenn+=1
            tem //= 10

        return ((i // (pow(10, lenn//2))), (i % (pow(10, lenn//2))) )

    else:
        return (i * 2024)

input = open('day11/inp.txt').read()
input = [int(item) for item in input.split()]
print(input)

cashe = {}
saved = {}

for num, i in enumerate(input):
    if not i in cashe.keys():
        cashe[i] = 1

print(cashe)

for _ in range(75):
    cloned = {}

    for i in cashe.keys():
        new = -1
        pop = cashe[i]
        
        if i in saved.keys():
            new = saved[i]
        else:
            new = logic(i)
            saved[i] = new

        if type(new) == tuple:
            if new[0] in cloned.keys():
                cloned[new[0]] += pop
            else:
                cloned[new[0]] = pop

            if new[1] in cloned.keys():
                cloned[new[1]] += pop
            else:
                cloned[new[1]] = pop
        else:
            if new in cloned.keys():
                cloned[new] += pop
            else:
                cloned[new] = pop
    
    cashe = cloned

print(sum(cashe.values()))
print(b)