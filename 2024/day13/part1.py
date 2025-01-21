input = open('day13/inp.txt').read().split("\n\n")

for num, i in enumerate(input):
    input[num] = i.split("\n")
    input[num] = [val.split(",") for val in input[num]]

    temp = []
    temp.append([int(input[num][0][0].split("+")[1]), int(input[num][0][1].split("+")[1])])
    temp.append([int(input[num][1][0].split("+")[1]), int(input[num][1][1].split("+")[1])])
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
    for x in range(min([yf//y1, yf//y2, xf//x1, xf//x2])):

        top = (x * (y1-x1)) + (xf - yf)
        bot = x2 - y2
        if bot == 0:
            xx = (xf-yf)/(x1-y1)
            yy = (yf - (y1*xx)) / y2
            temp.append([xx, yy])
            break

        possVal = top / bot
        if abs(possVal - round(possVal)) <= 0.01 and possVal >= 0 and possVal <= 100:
            temp.append([x, round(possVal)])
            
    
    minSum = 10000000000000000000000000000
    for j in temp:
        if (j[0]*3) + j[1] < minSum and (x1 * j[0]) + (x2 * j[1]) == xf and (y1 * j[0]) + (y2 * j[1]) == yf:
            minSum = (j[0]*3) + j[1]
    if not minSum == 10000000000000000000000000000:
        out += minSum
    print(i)


print(out)
# 25878