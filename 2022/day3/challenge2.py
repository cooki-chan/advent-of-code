input = ""
with open('day3/inp1.txt') as i:
    input = i.readlines()

priorityList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

totalPriority = 0
for i in range(0, int(len(input)/3)):
    string1 = input[i*3]
    string2 = input[i*3+1]
    string3 = input[i*3+2]

    hitNeededChar = False
    for i in string1:
        if i in string2 and i in string3 and not hitNeededChar:
            totalPriority += priorityList.index(i) + 1
            hitNeededChar = True

print(totalPriority)
