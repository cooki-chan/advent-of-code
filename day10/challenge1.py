input = ""
with open('day10/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

#Placeholder values to simplify calculations
status = [1, 1]
x = 1
for i in input:
    status.append(x)
    command = i.split(" ")
    if command[0] == "addx":
        x += int(command[1])
        status.append(x)
    print(status)

sum = 0
for i in range(6):
    sum += status[(i * 40) + 20] * ((i * 40) + 20)
    print(f"{status[(i * 40) + 20] * ((i * 40) + 20)} = {status[(i * 40) + 20]} * {((i * 40) + 20)}")

print(status[219])
print(sum)
