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
            if type(i) == int: #both int
                if type(right[index]) == int:
                    if i < right[index]:
                        return 1
                    elif i > right[index]:
                        return -1
                else: #right array
                    arrayI = list(i)
                    result = recursiveCheck(arrayI, right[index])
                    if result == 0:
                        continue
                    else:
                        return result
            elif type(i) == list:
                if type(right[index]) == int: #left array 
                    arrayR = list(right[index])
                    result = recursiveCheck(i, arrayR)
                    if result == 0:
                        continue
                    else:
                        return result
                else: #both array
                    result = recursiveCheck(i, right[index])
                    if result == 0:
                        continue
                    else:
                        return result
        except IndexError: #right shorter than left
            return -1
        index+=1
    
    if len(left) == len(right):
        return 0
    return 1

num = 0
for i in range(len(input)//3):
    if recursiveCheck(input[i*3], input[i*3+1]) == 1:
        num+=i+1

print(num)
