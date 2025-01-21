input = ""
with open('day10/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

#Placeholder values to simplify calculations
status = [1, 1]
x = 1
output = ""

def draw():
    global output
    currenPixel = len(status) % 40
    if x <= currenPixel and x >= currenPixel-2:
        output+=" # "
    else:
        output+=" . "
    if len(status) % 40 == 1:
        output+="\n"

for i in input:
    command = i.split(" ")
    if command[0] == "addx":
        draw()
        status.append(x)
        x += int(command[1])
    draw()
    status.append(x)

print(output)
