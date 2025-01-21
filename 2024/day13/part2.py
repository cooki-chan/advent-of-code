input = open('day13/inp.txt').read().split("\n\n")

for num, i in enumerate(input):
    input[num] = i.split("\n")
    input[num] = [val.split(",") for val in input[num]]

    temp = []
    temp.append([int(input[num][0][0].split("+")[1]), int(input[num][0][1].split("+")[1])])
    temp.append([int(input[num][1][0].split("+")[1]), int(input[num][1][1].split("+")[1])])
    #temp.append([int(input[num][2][0].split("=")[1]), int(input[num][2][1].split("=")[1])])

    temp.append([int(input[num][2][0].split("=")[1]) + 10000000000000, int(input[num][2][1].split("=")[1]) + 10000000000000])

    input[num] = temp

out = 0
for i in input:
#for i in [input[2]]:
#for i in [[[94, 34], [22, 67], [8400, 5400]]]:
    temp = []
    x1 = i[0][0]
    x2 = i[1][0]

    y1 = i[0][1]
    y2 = i[1][1]

    xf = i[2][0]
    yf = i[2][1]
    print(i)
    
    m1 = -x1/x2
    b1 = xf/x2

    m2 = -y1/y2
    b2 = yf/y2

    if m1 == m2:
        continue

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    print(x)
    print(y)

    if abs(x - round(x)) >= 0.001:
        continue

    if abs(y - round(y)) >= 0.001:
        continue

    out += x * 3 + y
    print(x * 3 + y)



print(out)
# 25878