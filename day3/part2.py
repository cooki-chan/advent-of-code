def findNumber(row, col):
    output = ""

    tempCol = col+1
    while input[row][tempCol].isdigit() and tempCol < len(input[row]):
        output += input[row][tempCol]
        tempCol+=1

    
    tempCol = col
    while input[row][tempCol].isdigit() and tempCol >= 0:
        output = input[row][tempCol] + output
        tempCol-=1
    
    return int(output)

q = open('day3/inp.txt')
input = q.readlines()

output = 0
for row in range(len(input)):
    trackNum = False
    number = ""
    for col in range(len(input[row])):
        if input[row][col] == "*":
            top = ""
            middle = ""
            bottom = ""

            if row-1 >= 0:
                if col-1 >= 0:
                    top += input[row-1][col-1]

                top +=input[row-1][col]

                if col+1 < len(input[row]):
                    top += input[row-1][col+1]
                
            if row+1 < len(input):
                if col-1 >= 0:
                    bottom += input[row+1][col-1]

                bottom +=input[row+1][col]

                if col+1 < len(input[row]):
                    bottom += input[row+1][col+1]

            if col-1 >= 0:
                middle += input[row][col-1]
            
            if col+1 < len(input[row]):
                middle += input[row][col+1]




            ratio =1
            times = 0
            for i in range(len(bottom)):
                if bottom[i].isdigit():
                    if len(bottom) == 2:
                        if input[row+1][col] == bottom[0]:
                            ratio *= findNumber(row+1,col+i)
                            times += 1
                        else:
                            ratio *= findNumber(row+1,col+i-1)
                            times += 1
                    else:
                        if (1+i < len(bottom) and not bottom[i+1].isdigit()) or (i-1 >= 0 and not bottom[i-1].isdigit()) or (1+i < len(bottom) and i-1 >= 0 and (bottom[i-1].isdigit()) and bottom[i+1].isdigit()):
                            ratio *= findNumber(row+1,col-1+i)
                            times += 1

            for i in range(len(top)):
                if top[i].isdigit():
                    if len(top) == 2:
                        if top[row-1][col] == top[0]:
                            ratio *= findNumber(row-1,col+i)
                            times += 1
                        else:
                            ratio *= findNumber(row-1,col+i-1)
                            times += 1
                    else:
                        if (1+i < len(top) and not top[i+1].isdigit()) or (i-1 >= 0 and not top[i-1].isdigit()) or (1+i < len(top) and i-1 >= 0 and (top[i-1].isdigit()) and top[i+1].isdigit()):
                            ratio *= findNumber(row-1,col-1+i)
                            times += 1
            
            if middle[0].isdigit():
                ratio *= findNumber(row,col-1)
                times += 1

            if middle[1].isdigit():
                ratio *= findNumber(row,col+1)
                times += 1
            
            if times == 2:
                output += ratio

            
print(output)








