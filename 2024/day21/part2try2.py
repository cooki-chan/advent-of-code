import copy

input = open('day21/inp.txt').read().split('\n')
#input = ["A980A"]
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
    up = {"A":">", ">":"v>", "v":"v", "<":"v<"} #1,2,1,2
    down = {"<":"<", "^":"^", ">":">", "A":"^>"} #1,1,1,2
    right = {"A":"^", "^":"^<", "v":"<", "<":"<<"}
    left = {"v":">", "^":">^", ">":">>", "A":">>^"}
    a = {"^":"<", "v":"v<", ">":"v", "<":"v<<"}

    if curr == target:
        return "A"
    
    out = {}
    outStr = ""
    match curr:
        case "^":
            outStr = up[target] + "A"
        case ">":
            outStr = right[target] + "A"
        case "<":
            outStr = left[target] + "A"
        case "v":
            outStr = down[target] + "A"
        case "A":
            outStr = a[target] + "A"
    
    for i in outStr:
        if i not in out.keys():
            out[i] = outStr.count(i)
    return out


#print(keypad_to_arrow("A", "7"))

#keypad to arrow layer
temp = []
for ind, i in enumerate(input):
    out = []
    for j in range(len(i)-1):
        out.append(keypad_to_arrow(str(i[j]), str(i[j+1])))
    temp.append(out)
input = temp

print(input)

#arrow to arrow layer 1
for cod, code in enumerate(input):
    for position, allPos in enumerate(code):
        for posNum, pos in enumerate(allPos):
            t = {}
            for j in "^v<>A":
                t[j] = 0

            temp = keypad_to_keypad("A", pos[0])

            for j in temp.keys():
                t[j] += temp[j]

            for i in range(len(pos)-1):
                temp = keypad_to_keypad(pos[i], pos[i+1])

                if temp == "A":
                    t["A"] +=1
                else:
                    for j in temp.keys():
                        t[j] += temp[j]
            input[cod][position][posNum] = t

print(input)
# rest of the needed iterations
iters = 25
for _ in range(iters-1):
    for cod, code in enumerate(input):
        for position, allPos in enumerate(code):
            for posNum, pos in enumerate(allPos):
                new = {}
                for j in "^v<>A":
                    new[j] = 0
                
                for i in pos.keys():
                    goto = keypad_to_keypad("A", i)
                    if goto == "A":
                        new["A"] += 1
                    else:
                        for j in goto.keys():
                            new[j] += goto[j] * pos[i]

                    goback = keypad_to_keypad(i, "A")
                    if goback == "A":
                        new["A"] += 1
                    else:
                        for j in goback.keys():
                            new[j] += goback[j] * pos[i]
                    
                new["A"] = sum(pos.values())
                input[cod][position][posNum] = new
                print(new)
    print(input)

out = []
for cod, code in enumerate(input):
    total = 0
    for position, allPos in enumerate(code):
        lowest = 999999999999999999999999999
        for posNum, pos in enumerate(allPos):
            s = sum(pos.values())
            if s < lowest:
                lowest = s
        total += lowest

    out.append(total)
print(sum(out))