input = open('day11/inp.txt').read()
input = [int(item) for item in input.split()]
print(input)

for _ in range(75):
    print(_)
    temp = []
    for num, i in enumerate(input):
        if i == 0:
            temp.append(1)
        
        elif len(str(i)) % 2 == 0:
            temp.append(int(str(i)[0:int(len(str(i))/2)]))
            temp.append(int(str(i)[int(len(str(i))/2):len(str(i))]))

        else:
            temp.append(i * 2024)
    input = temp

print(len(input))
