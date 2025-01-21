input = ""
with open('day3/inp1.txt') as i:
    input = i.readlines()

priorityList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

totalPriority = 0
for i in input:
    initString = i

    if "\n" in i:
        initString = i.replace("\n", "")
    
    string1 = initString[0:int(len(initString)/2)]
    string2 = initString[int(len(initString)/2):len(initString)]

    hitNeededChar = False
    for i in string1:
        if i in string2 and not hitNeededChar:
            totalPriority += priorityList.index(i) + 1
            hitNeededChar = True

print(totalPriority)
