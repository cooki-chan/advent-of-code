input = open('day4/inp.txt').read().split('-')

s = int(input[0])
e = int(input[1])
count = []

curr = s-1
while not curr == e:
    curr+=1
    if len(set(str(curr))) >= len(str(curr)):
        correct = False
        continue
    
    sc = str(curr)
    sc2 = "0" + sc + "0"
    hasTwo = False
    for i in range(len(sc)-1):
        if int(sc[i]) > int(sc[i+1]):
            hasTwo = False
            break
        
        check = sc2[i:i+4]
        if sc2[1+i] == sc2[2+i] and not sc2[0+i] == sc2[1+i] and not sc2[1+i] == sc2[3+i]:
            hasTwo = True
        


    

    if hasTwo:
        count.append(curr)

print(len(count))