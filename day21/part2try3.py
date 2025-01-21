input = ["A" + i for i in open('day21/inp.txt').read().split('\n')]
#input = ["A1A"]
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

            #left:
            if pos[1] > 0 and not graph[pos[0]][pos[1]-1] == "X":
                td = dist([pos[0], pos[1]-1], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + "<", [pos[0], pos[1]-1]])

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

            #right:
            if pos[1] < 2:
                td = dist([pos[0], pos[1]+1], targetPos)
                if td < dist(pos, targetPos):
                    new.append([currPath + ">", [pos[0], pos[1]+1]])
            
            working.remove(i)
            working += new
    return out

def keypad_to_keypad(curr, target):
    up = {"A":">", ">":"v>", "v":"v", "<":"v<", "^":""} #1,2,1,2
    down = {"<":"<", "^":"^", ">":">", "A":"^>", "v":""} #1,1,1,2
    right = {"A":"^", "^":"<^", "v":"<", "<":"<<", ">":""}
    left = {"v":">", "^":">^", ">":">>", "A":">>^", "<":""}
    a = {"^":"<", "v":"<v", ">":"v", "<":"v<<", "A":""}

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
    
    return outStr


#print(keypad_to_arrow("A", "7"))

#keypad to arrow layer
temp = []
for ind, i in enumerate(input):
    out = []
    for j in range(len(i)-1):
        out.append(keypad_to_arrow(str(i[j]), str(i[j+1])))
    temp.append(out)
input = temp

#input = [[['^^^<<A'], ['>>vvvA']]]
print(input)

#translation to simplified format
for cod, code in enumerate(input):
    for position, allPos in enumerate(code):
        for posNum, pos in enumerate(allPos):
            new = {f"A{pos[0]}":1}
            for char in range (len(pos)-1):
                if pos[char] + pos[char+1] in new.keys():
                    new[pos[char] + pos[char+1]] += 1
                else:
                    new[pos[char] + pos[char+1]] = 1
            input[cod][position][posNum] = new
            if pos == "A":
                input[cod][position][posNum] = {"AA":1}

print(input)

for _ in range(25):
    print()
    print(_)
    for cod, code in enumerate(input):
        for position, allPos in enumerate(code):
            for posNum, pos in enumerate(allPos):
                new = {}
                for combo in pos.keys():
                    nextLayer = "A" + keypad_to_keypad(combo[0], combo[1])
                    #print(nextLayer)

                    for char in range (len(nextLayer)-1):
                        #print(nextLayer[char] + nextLayer[char+1])
                        if nextLayer[char] + nextLayer[char+1] in new.keys():
                            new[nextLayer[char] + nextLayer[char+1]] += pos[combo]
                        else:
                            new[nextLayer[char] + nextLayer[char+1]] = pos[combo]
                    #print(new)
                    #print()

                input[cod][position][posNum] = new

print(input)

out = 0
for cod, code in enumerate(input):
    tempOUT = 0
    for position, allPos in enumerate(code):
        lowest = 999999999999999999999999999999999999
        for posNum, pos in enumerate(allPos):
            print(lowest)
            if sum(pos.values()) < lowest:
                lowest = sum(pos.values())
        tempOUT += lowest
    out += tempOUT * int(inp[cod][1:len(inp[cod])-1])

print(out)


#[['v<A<A>>^Av<<A>>^AAvAA^<A>Av<A^>A<Av<A>>^AvA^Av<A<A>>^Av<<A>>^AvAA^<A>Av<A^>AA<Av<A>>^AvA^A', 'v<A<AA>>^AvAA^<A>Av<A<A>>^Av<<A>>^AvAA^<A>AAv<A^>AA<Av<A>>^AvA^A'], ['v<A<A>>^A<Av>A^Av<A<AA>>^AvAA^<A>Av<A^>A<A>Av<<A>>^AvA^A', 'v<A<A>>^A<Av>A^AAv<A<AA>>^AvAA^<A>Av<<A>>^Av<A>A^A<A>A']]