input = ""
with open('day4/inp1.txt') as i:
    input = i.readlines()

numOverlap = 0
for i in input:
    if "\n" in i:
        i = i.replace("\n", "")
    string = i[0:len(i)].split(",")

    elf1 = string[0].split("-")
    elf1 = [int(x) for x in elf1]

    elf2 = string[1].split("-")
    elf2 = [int(x) for x in elf2]

    if (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or (elf1[1] >= elf2[0] and elf1[1] <= elf2[1]):
        numOverlap+=1
    elif (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]) or (elf2[1] >= elf1[0] and elf2[1] <= elf1[1]):
            numOverlap+=1

print(numOverlap)
