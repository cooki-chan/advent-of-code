import copy

input = open('day21/inp.txt').read().split('\n')
input = ["A2A"]
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

for _ in range(3):
    print(_)
    for code, i in enumerate(input):
        for pos, j in enumerate(i):
            for poss, k in enumerate(j):
                rep = keypad_to_keypad("A", k[0])
                for l in range(len(k)-1):
                    rep += keypad_to_keypad(k[l], k[l+1])
                input[code][pos][poss] = rep
    print(input)

out = 0
for code, i in enumerate(input):
    print(i)
    ID = int(inp[code][1:len(inp[code])-1])

    count = 0
    for j in i:
        count += len(min(j, key=len))
        #print(len(min(j, key=len)))
    print(str(ID) + " * " + str(count))
    out += ID * count
print(out)