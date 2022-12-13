input = ""
with open('day11/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

monkies = []

class monkey:
    def __init__(self, startItems, operation, test:str, true, false):
        exec(f"self.items = [{startItems.split(': ')[1]}]")
        self.operation = operation.split("old ")[1].split(' ')[0]
        self.opValue = operation.split("old ")[1].split(' ')[1]
        
        if self.opValue.isdigit():
            self.opValue = int(self.opValue)
        self.test = int(test.split(' ')[5])
        self.true = int(true.split(" ")[9])
        self.false = int(false.split(" ")[9])
        self.noInspected = 0

    def recieve(self, item):
        self.items.append(item)
    
    def toss(self): 
        for old in self.items:
            tempWorry = old
            operationVal = 0
            if type(self.opValue) == int:
                operationVal = self.opValue
            else:
                operationVal = old
            match self.operation:
                case "+":
                    tempWorry += operationVal
                case "*":
                    if type(operationVal) != type(self.opValue):
                        print("slowwwwww")
                        tempWorry = operationVal**2
                    else:
                        tempWorry = old * operationVal
            self.noInspected+=1
            if tempWorry % self.test == 0:
                monkies[self.true].recieve(tempWorry)
            else:
                monkies[self.false].recieve(tempWorry)
        self.items = []

for i in range(4):
    currentMonkey = i * 7
    monkies.append(monkey(input[currentMonkey+1], input[currentMonkey+2], input[currentMonkey+3], input[currentMonkey+4], input[currentMonkey+5]))

for i in range(10000):
    for j in range(len(monkies)):
        monkies[j].toss()
        print("tossed")
    #for j in range(len(monkies)):
        #print(f"{j}: {monkies[j].items} with {monkies[j].noInspected}")
    print(f"{i}!!!")

biggestVals = []
for i in monkies:
    biggestVals.append(i.noInspected)

print(biggestVals)
biggestVals.sort(reverse=True)
print(biggestVals[0] * biggestVals[1])
