i = open('day4/inp.txt')
input = i.readlines()

for i in range(len(input)):
    input[i] = input[i].split(":")[1]

output = 0
for i in input:
    parsed = i.split("| ")
    winningNums = parsed[0]
    losingNums = parsed[1]

    pointsWon = 0
    for i in losingNums.split(" "):
        if "\n" in i:
            i = i[0:len(i)-1]

        if " "+i+" " in winningNums and not i == "":
            if pointsWon == 0:
                pointsWon = 1
            else:
                pointsWon *= 2
    
    output += pointsWon

print(output)

