import random

input = ""
with open('day7/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

#input is list of commands

directory = {}
currentDir = []

for i in input:
    if i[0] == "$":
        if i[2:4] == "cd":
            match(i.replace("$ cd ", "")):
                case "/":
                    currentDir = []
                case "..":
                    currentDir.pop()
                case _:
                    currentDir.append(i.replace("$ cd ", ""))

    else:
        if i[0:3] == "dir":
            values = i.split(" ")
            addDir = "directory"
            for i in currentDir:
                addDir += f"['{i}']"

            addDir += f"['{values[1]}'] = " + "{}"
            exec(addDir)

        else:
            values = i.split(" ")
            addDir = "directory"
            for i in currentDir:
                addDir += f"['{i}']"

            addDir += f"['{values[1]}'] = {values[0]}"
            exec(addDir)

allDirectories = []
def recursiveDirSearch(directory):
    dirVal = 0

    for i in directory.keys():
        if type(directory[i]) == dict:
            dirVal += recursiveDirSearch(directory[i])
        else:
            dirVal += directory[i]
        
    allDirectories.append(dirVal)
    return dirVal
recursiveDirSearch(directory)

spaceUsed = allDirectories[len(allDirectories)-1]
spaceNeedDel = ((70000000 - spaceUsed) - 30000000) * -1

closestVal = 999999999999
for i in allDirectories:
    if i > spaceNeedDel and i < closestVal:
        closestVal = i


print(closestVal)
