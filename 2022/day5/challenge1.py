from queue import LifoQueue as Stack

input = ""
with open('day5/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")


#EXTRA CHALLENGE!!! AS LITTLE HARD CODING AS POSSIBLE!!!
stacks = []

#Stack Setup
for i in range(int(len(input[0])+1) // 4):
    stacks.append(Stack())

#Input Stacks
index = 0
while " 1  " not in input[index]:
    line = input[index]

    currentStack = 0
    for i in stacks:
        if line[currentStack * 4 + 2] != " ":
            i.put(line[currentStack * 4 + 1])
        currentStack+=1
    index+=1


#Flip Stacks
index = 0
for i in stacks:
    flipped = Stack()

    while not i.empty():
        get = i.get()
        flipped.put(get)
        print(get)
    print(i)
    stacks[index] = flipped
    index+= 1

#movement
for i in input:
    if "move" in i:
        words = i.split(" ")
        print(words)

        numMoved = int(words[1])
        originStack = int(words[3]) - 1
        destinationStack = int(words[5]) - 1

        for i in range(0, numMoved):
            moved = stacks[originStack].get()
            stacks[destinationStack].put(moved)
            

out = ""
for i in stacks:
    out+= i.get()

print(out)
