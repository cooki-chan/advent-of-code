input = ""
with open('day1/inp1.txt') as i:
    input = i.readlines()

highest = 0
tempVal = 0
for i in input:
    if i != "\n":
        tempVal += int(i.replace("\n", ""))
    else: #end of a section
        if tempVal > highest:
            highest = tempVal
        tempVal = 0

print(highest)