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

out = 0
for i in range(len(input)):
    if recursiveCheck(json.loads(input[i*3]), json.loads(input[i*3+1])) == 1:
        out+=i+1

print(out)