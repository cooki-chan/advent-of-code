input = ""
with open('day1/inp1.txt') as i:
    input = i.readlines()

highest = 0
tempVal = 0
for i in input:
    if i != "\n":
        if "\n" in i: #litterly only exists for the sole purpouse of that one line at the end without a \n
            tempVal += int(i[0:len(i) - 1])
        else:
            tempVal += int(i)

    else: #end of a section
        if tempVal > highest:
            highest = tempVal
        tempVal = 0

print(highest)

