input = open('day3/inp.txt').read().split('\n')

line1 = set()
line2 = set()

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
    
    for j in range(int(i[1:])+1):
        line1.add(currPos + (j * d))
    currPos = currPos + (j * d)
    

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
    
    for j in range(int(i[1:])+1):
        line2.add(currPos + (j * d))
    currPos = currPos + (j * d)
inters = line1.intersection(line2)
inters.remove(0j)
print(inters)

lowest = 99999999999
for i in inters:
    if abs(i.real) + abs(i.imag) < lowest:
        lowest = abs(i.real) + abs(i.imag)
        print(i)
print(lowest)
#print(line1)