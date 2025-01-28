input = open('day3/inp.txt').read().split('\n')

line1 = []
line2 = []

currPos = 0+0j
for i in input[0].split(","):
    d = 0+0j
    match i[0]:
        case "U":
            d = 0+1j
        case "D":
            d = 0-1j
        case "R":
            d = 1+0j
        case "L":
            d = -1+0j
    
    for j in range(1,int(i[1:])+1):
            line1.append(currPos + (j * d))
    currPos = currPos + (j * d)
    
print(0)
currPos = 0+0j
for i in input[1].split(","):
    d = 0+0j
    match i[0]:
        case "U":
            d = 0+1j
        case "D":
            d = 0-1j
        case "R":
            d = 1+0j
        case "L":
            d = -1+0j
    
    for j in range(1,int(i[1:])+1):
            line2.append(currPos + (j * d))
    currPos = currPos + (j * d)
inters = set(line1).intersection(set(line2))
print(inters)

lowest = 99999999999
for i in inters:
    if line1.index(i) + line2.index(i) < lowest:
        lowest = line1.index(i) + line2.index(i)
        print(i)
print(lowest+2)