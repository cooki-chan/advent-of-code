input = open('09/inp.txt').read().split('\n')

input = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in input]

def check(pair, checked):
    Xs = [pair[0][0], pair[1][0]]
    Ys = [pair[0][1], pair[1][1]]
    if min(Xs) < checked[0] < max(Xs) and min(Ys) < checked[1] < max(Ys):
        return True
    return False

def a(x):
    return (abs(x[0][0]-x[1][0])+1) * (abs(x[0][1]-x[1][1])+1)

n = input.copy()
for i in range(len(input)-1):
    #print(n)
    first = input[i]
    second = input[i+1]

    if first[0] != second[0]:
        x = [first[0], second[0]]
        n += [(j, first[1]) for j in range(min(x)+1, max(x))]
    else:
        x = [first[1], second[1]]
        n += [(first[0], j) for j in range(min(x), max(x)+1)]

first = input[-1]
second = input[0]

if first[0] != second[0]:
    x = [first[0], second[0]]
    n += [(j, first[1]) for j in range(min(x)+1, max(x))]
else:
    x = [first[1], second[1]]
    n += [(first[0], j) for j in range(min(x), max(x)+1)]

pairs = []
for i in input:
    for j in input[input.index(i)+1:]:
        pairs.append((i, j))

possible = []
for ind, i in enumerate(pairs):
    print(ind, len(pairs))
    passed = True
    for j in n:
        if check(i, j):
            passed = False
            break
    if passed:
        possible.append(i)

possible.sort(key = lambda x: a(x), reverse = True)
print(possible)
x = possible[0]
print(a(x))
print(x)

# for i in n:
#     print(check(x,i), i)