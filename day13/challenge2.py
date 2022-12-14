import json

input = ""
with open('day13/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

#returns 1 for correct, -1 for not, 0 for tie
def recursiveCheck(left, right):
    index = 0
    for i in left:
        try:
            print(i)
            print(right[index])
            print("--")
            if type(i) == int: #both int
                if type(right[index]) == int:
                    if i < right[index]:
                        return 1
                    elif i > right[index]:
                        return -1
                else: #right array
                    arrayI = [i]
                    result = recursiveCheck(arrayI, right[index])
                    if not result == 0:
                        return result
            elif type(i) == list:
                if type(right[index]) == int: #left array 
                    arrayR = [right[index]]
                    result = recursiveCheck(i, arrayR)
                    if not result == 0:
                        return result
                else: #both array
                    result = recursiveCheck(i, right[index])
                    if not result == 0:
                        return result
        except IndexError: #right shorter than left
            return -1
        index+=1
    
    if len(left) == len(right):
        return 0
    return 1

validPak = []
for i in range(len(input)//3 + 1):
    validPak.append(json.loads(input[i*3]))
    validPak.append(json.loads(input[i*3+1]))
validPak.append([[2]])
validPak.append([[6]])

sorted = False
while not sorted:
    sorted = True
    for i in range(len(validPak)-1):
        if not recursiveCheck(validPak[i], validPak[i+1]) == 1:
            sorted = False
            temp = validPak[i+1]
            validPak[i+1] = validPak[i]
            validPak[i] = temp
        else:
            print("pass")

div2 = 0
div6 = 0
for i in range(len(validPak)):
    if validPak[i] == [[2]]:
        div2 = i+1
    if validPak[i] == [[6]]:
        div6 = i+1
    print(validPak[i])

print(div2)
print(div6)
print(div2 * div6)