input = open('day21/inp.txt').read().split('\n')
input = ["A980A"]
inp = input.copy()

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def keypad_to_arrow(curr, target):
    currPos = [-1, -1]
    targetPos = [-1, -1]

    graph = [("7","8","9"),("4","5","6"),("1","2","3"),("X","0","A")]
    for row, i in enumerate(graph):
        for col, j in enumerate(i):
            if str(curr) == j or curr == j:
                currPos = [row, col]
            if str(target) == j or target == j:
                targetPos = [row, col]
    
    
    out = []
    working = [["", currPos.copy()]]
    while not working == []:
        for i in working:
            new = []
            pos = i[1]
            currPath = i[0]

            if dist(i[1], targetPos) == 0:
                out.append(i[0] + "A")
                working.remove(i)
                continue

            #up:
            if pos[0] > 0:
                td = dist([pos[0]-1, pos[1]], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + "^", [pos[0]-1, pos[1]]])

            #down:
            if pos[0] < 3 and not graph[pos[0]+1][pos[1]] == "X":
                td = dist([pos[0]+1, pos[1]], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + "v", [pos[0]+1, pos[1]]])
            
            #left:
            if pos[1] > 0 and not graph[pos[0]][pos[1]-1] == "X":
                td = dist([pos[0], pos[1]-1], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + "<", [pos[0], pos[1]-1]])

            #right:
            if pos[1] < 2:
                td = dist([pos[0], pos[1]+1], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + ">", [pos[0], pos[1]+1]])
            
            working.remove(i)
            working += new
    return out

def keypad_to_keypad(curr, target):
    up = {"A":">", ">":">v", "v":"v", "<":"v<"} #1,2,1,2
    down = {"<":"<", "^":"^", ">":">", "A":">^"} #1,1,1,2
    right = {"A":"^", "^":"<^", "v":"<", "<":"<<"}
    left = {"v":">", "^":">^", ">":">>", "A":">>^"}
    a = {"^":"<", "v":"<v", ">":"v", "<":"v<<"}

    if curr == target:
        return "A"
    
    match curr:
        case "^":
            return up[target] + "A"
        case ">":
            return right[target] + "A"
        case "<":
            return left[target] + "A"
        case "v":
            return down[target] + "A"
        case "A":
            return a[target] + "A"
    
    raise ValueError(f"what the actual fuck {curr} -> {target}")


#print(keypad_to_arrow("A", "7"))

temp = []
for ind, i in enumerate(input):
    out = []
    for j in range(len(i)-1):
        out.append(keypad_to_arrow(str(i[j]), str(i[j+1])))
    temp.append(out)
input = temp

for code, i in enumerate(input):
    for pos, j in enumerate(i):
        temp = []
        for poss, k in enumerate(j):
            temp.append({k:1})

        input[code][pos] = temp

print(input)

#input = [[[{"<^>vA":1}], [{"^<A":1}, {"<^A":1}]]]

for _ in range(10):
    print(_)
    for code, i in enumerate(input):
        for pos, j in enumerate(i):
            for poss, k in enumerate(j):
                temp = {}
                for key in k.keys():
                    if key == "A":
                        temp["A"] += k[key]
                        continue

                    rep = keypad_to_keypad("A", key[0])
                    for l in range(len(key)-1):
                        rep += keypad_to_keypad(key[l], key[l+1])

                    if not len(key) == 1:
                        rep += keypad_to_keypad(key[l+1], "A")
                    else:
                        rep += keypad_to_keypad(key[0], "A")

                    rep2 = rep
                    rep3 = rep[0:len(rep)-1]
                    rep = rep.split("A")
                    ke = list(set(rep))
                    ke = sorted(ke, key=len, reverse=True)
                    for kee in ke:
                        #print("|" + kee + "|")

                        if not kee == "":
                            if kee + "A" in temp.keys() and kee + "A" in rep2:
                                temp[kee + "A"] += rep2.count(kee) * k[key]
                            else:
                                temp[kee + "A"] = rep2.count(kee) * k[key]
                            
                        rep2 = rep2.replace(kee + "A", "")
                    
                    As = 0
                    print(rep3)
                    for ind in range(len(rep3)-1):
                        if rep3[ind] == "A" and rep3[ind+1] == "A":
                            As+=k[key]
                    if "A" not in temp.keys():
                        temp["A"] = As
                    else:
                        temp["A"] += As
                    print("As: " + str(As))
                    print()

                
                input[code][pos][poss] = temp
                print(temp)
        print(input)

print()
out = 0
for code, i in enumerate(input):
    score = 0

    for pos, j in enumerate(i):
        lowest = 10000000000000

        for poss, k in enumerate(j):
            sum = 0

            for key in k.keys():
                sum += len(key) * k[key]

            if sum < lowest:
                lowest = sum
        score += lowest
        print(sum)
        print()
    # print(score)
    # print()

    ID = int(inp[code][1:len(inp[code])-1])
    out += score * ID
print(out)



# [['<vA<AA>>^AvAA<^A>A'], 
# ['v<<A>>^AvA^A'], 
# ['v<<A>>^AAvA<A>^A<A>A', '<vA>^Av<<A>^A>AAvA^A', 'v<<A>>^AvA<A>^Av<<A>^A>AvA^A'], 
# ['v<<A>A>^AAAvA<^A>A']]



# [{'v<<A': 1, '>^A': 2, '>A': 1, 'A': 1, '<vA': 1, 'vA': 1, '^A': 1}, {'>^A': 2, 'vA': 2, '<A': 1, 'A': 0, 'v<<A': 2, '>A': 1, '>>^A': 1, '^A': 1}], 
# [{'v<<A': 1, '>^A': 1, '>A': 2, 'A': 2, '<^A': 1, 'vA': 1}]]]