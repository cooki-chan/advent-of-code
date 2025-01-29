input = open('day4/inp.txt').read().split('-')

s = int(input[0])
e = int(input[1])
count = []

curr = s
while not curr == e:
    curr+=1
    #print(curr)
    correct = True
    if len(set(str(curr))) >= len(str(curr)):
        correct = False
    
    sc = str(curr)
    for i in range(len(sc)-1):
        if int(sc[i]) > int(sc[i+1]):
            correct = False
    if correct:
        count.append(curr)

print(len(count))