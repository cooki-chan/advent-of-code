input = ""
with open('day1/inp1.txt') as i:
    input = i.readlines()

#1st, 2nd, 3rd
highest = [0, 0, 0]
tempVal = 0
for i in input:
    if i != "\n":
        tempVal += int(i.replace("\n", ""))

    else: #end of a section
        for i in range(0, 2):
            if tempVal >= highest[i]:
                highest.insert(i, tempVal)
                highest.pop()
                tempVal = 0
        tempVal = 0

print(highest[0] + highest[1] + highest[2])