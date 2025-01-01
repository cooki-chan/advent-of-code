input = open('day24/inp.txt').read().split('\n\n')
input[0] = input[0].split("\n")
input[1] = input[1].split("\n")

bits = {}

for i in input[0]:
    bits[i.split(":")[0]] = int(i.split(":")[1])

#HAND VERIFIED
carryIndex = "tss"

def errorFinder(first, second):
    for i in input[1]:
        if first in i:
            print(i)
    print()
    for i in input[1]:
        if second in i:
            print(i)

for currBit in range(1, 45, 1):

    firstXOR = ""
    firstAND = ""
    for i in input[1]:
        if "x" + "{:02d}".format(currBit) in i and "y" + "{:02d}".format(currBit) in i and " XOR " in i:
            firstXOR = i.split(" -> ")[1]
        
        if "x" + "{:02d}".format(currBit) in i and "y" + "{:02d}".format(currBit) in i and " AND " in i:
            firstAND = i.split(" -> ")[1]
    print(f"firstXOR = {firstXOR}, firstAND = {firstAND}")

    if "z" in firstAND:
        print(f"ERROR: Z detected in firstAND {firstAND}.")
        errorFinder(firstAND, firstAND)

    if "z" in firstXOR:
        print(f"ERROR: Z detected in firstXOR {firstXOR}.")
        errorFinder(firstXOR, firstXOR)

    S = ""
    secondAND = ""
    for i in input[1]:
        if firstXOR in i and carryIndex in i and " XOR " in i:
            S = i.split(" -> ")[1]
        if firstXOR in i and carryIndex in i and " AND " in i:
            secondAND = i.split(" -> ")[1]
    print(f"S = {S}, secondAND = {secondAND}")
    
    if S == "" or secondAND == "":
        print(f"ERROR: {firstXOR} or {carryIndex} is incorrect. Source: S")
        errorFinder(firstXOR, carryIndex)
        raise ValueError(f"{currBit}")
    if "z" not in S:
        print(f"ERROR: {firstXOR} XOR {carryIndex} is not a z value")
        errorFinder(firstXOR, carryIndex)
        raise ValueError(f"{currBit}")
    if "z" in secondAND:
        print(f"ERROR: Z detected in econdAND {secondAND}.")
        errorFinder(secondAND, secondAND)

    cout = ""
    for i in input[1]:
        if secondAND in i and firstAND in i and " OR " in i:
            cout = i.split(" -> ")[1]
    print(f"cout = {cout}")

    if "z" in cout:
        print(f"ERROR: Z detected in cout {cout}.")
        errorFinder(cout, cout)
    
    if cout == "":
        print(f"ERROR: {secondAND} or {firstAND} is incorrect. source: cout")
        errorFinder(secondAND, firstAND)
        raise ValueError(f"{currBit}")
    else:
        carryIndex = cout
    print("----------------------------------------------------")




