input = ""
with open('day11/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

monkies = []

class monkey:

    def __init__(self, startItems, operation, test:str, true, false):
        exec(f"self.items = [{startItems.split(': ')[1]}]")
        self.operation = operation.split("old ")[1]
        self.test = int(test.split(' ')[5])
        self.true = int(true.split(" ")[9])
        self.false = int(false.split(" ")[9])
        self.noInspected = 0

    def recieve(self, item):
        self.items.append(item)
    
    def toss(self):
        for old in self.items:
            tempWorry = eval(f"{old} {self.operation} / 3")
            if tempWorry % self.test == 0:
                monkies[self.true].recieve(tempWorry)
            else:
                monkies[self.false].recieve(tempWorry)
            self.items.remove(old)
            self.noInspected+=1

for i in range(8):
    currentMonkey = i * 7
    monkies.append(monkey(input[currentMonkey+1], input[currentMonkey+2], input[currentMonkey+3], input[currentMonkey+4], input[currentMonkey+5]))

for i in range(20):
    for j in range(len(monkies)):
        monkies[j].toss()
        print(j)
    print(f"{i}!!!")

biggestVals = []
for i in monkies:
    biggestVals.append(i.noInspected)

biggestVals.sort(reverse=True)
print(biggestVals[0] * biggestVals[1])
