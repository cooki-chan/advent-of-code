import math

input = ""
with open('day9/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

head = [0, 0] #x, y
tail = [0, 0]

def moveTail():
    dist = math.sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2) #dist formula

    if dist >= 2.0: #tail needs to move
        if head[1] > tail[1]:   #head is higher, tail must move up
            tail[1]+=1
        elif head[1] < tail[1]: #tail is higher, must move down
            tail[1]-=1

        if head[0] > tail[0]:   #head is right, tail mush move right
            tail[0]+=1
        elif head[0] < tail[0]: #tail is right, tail must move left
            tail[0]-=1

tailVisited = set() #t

for i in input:
    command = i.split(" ")
    for i in range(int(command[1])):
        match command[0]:
            case "R":
                head[0]+=1
            case "L":
                head[0]-=1
            case "U":
                head[1]+=1
            case "D":
                head[1]-=1
        moveTail()
        print(str(tail) + ", " + str(head))
        tailVisited.add(tuple(tail))

print(len(tailVisited))
    

