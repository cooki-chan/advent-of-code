input = open('09/inp.txt').read().split('\n')

input = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in input]

lines = []
for i in range(len(input)-1):
    lines.append((input[i], input[i+1]))
lines.append((input[-1], input[0]))

def a(x):
    return (abs(x[0][0]-x[1][0])+1) * (abs(x[0][1]-x[1][1])+1)

pairs = []
for i in input:
    for j in input[input.index(i)+1:]:
        pairs.append((i, j))

pairs.sort(reverse=True, key = a)

def check(box, line):
    Xs = [box[0][0], box[1][0]]
    Ys = [box[0][1], box[1][1]]
    if min(Xs) < line[0][0] < max(Xs) and min(Ys) < line[0][1] < max(Ys):
        return True
    if min(Xs) < line[1][0] < max(Xs) and min(Ys) < line[1][1] < max(Ys):
        return True


    #ver line
    if line[0][0] == line[1][0]:
        if min(Xs) < line[0][0] < max(Xs):
            l = list(line)
            l.sort(key = lambda x: x[1])
            if l[0][1] <= min(Ys) and l[1][1] >= max(Ys):
                return True
    #hori line
    else:
        if min(Ys) < line[0][1] < max(Ys):
            l = list(line)
            l.sort(key = lambda x: x[0])
            if l[0][0] <= min(Xs) and l[1][0] >= max(Xs):
                return True
            
    return False

sqrs = ()
for ind, i in enumerate(pairs):
    print(ind, len(pairs))
    passed = True
    for j in lines:
        if check(i, j):
            passed = False
            break
    if passed:
        sqrs = i
        break

print(a(sqrs))
print(sqrs)