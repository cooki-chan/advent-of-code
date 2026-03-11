input = open('10/inp.txt').read().split('\n')

input = [i.split(" ") for i in input]

for ind, i in enumerate(input):
    new = []
    for j in i:
        if '[' in j:
            s = j[1:len(j)-1]
            s = s.replace("#", "1")
            s = s.replace(".", "0")
            new.append(int(s[::-1], 2))

        if '(' in j:
            s = j[1:len(j)-1]
            out = [2 ** (int(i)) for i in s.split(",")]
            new.append(sum(out))

    input[ind] = new

def check(possibles, buttons):
    new = set()
    for j in possibles: #afters
        for k in buttons: #buttons
            if j ^ k != 0:
                new.add(j ^ k)
            else:
                return 1
    return new

out = 0
for i in input:
    possibles = set([i[0]])
    iters = 1
    while True:
        found = False
        test = check(possibles, i[1:])
        if test == 1:
            break
        else:
            possibles = test
        iters+=1
    out+=iters

print(out)