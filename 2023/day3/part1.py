q = open('day3/inp.txt')
input = q.readlines()

output = 0
for row in range(len(input)):
    trackNum = False
    number = ""
    for col in range(len(input[row])):
        if input[row][col].isdigit():
            trackNum = True
            number += input[row][col]
        elif trackNum:
            surrounding = ""

            if trackNum:
                if row-1 >= 0:
                    surrounding += input[row-1][col-len(number):col]
                    if col-1-len(number) >= 0:
                        surrounding += input[row-1][col-1-len(number):col-len(number)]
                
                    if col+1 < len(input[row]):
                        surrounding += input[row-1][col]
                


                if row+1 < len(input):
                    surrounding += input[row+1][col-len(number):col]

                    t = col-1-len(number)
                    if col-1-len(number) >= 0:
                        surrounding += input[row+1][col-len(number)-1:col-len(number)]
                
                    if col+1 < len(input[row]):
                        surrounding += input[row+1][col]
                


                if col-1-len(number) >= 0:
                    surrounding += input[row][col-1-len(number):col-len(number)]
                
                if col+1 < len(input[row]):
                    surrounding += input[row][col]

                
                
                for i in surrounding:
                    if not i.isdigit() and not i == ".":
                        output += int(number)

            trackNum = False
            number = ""


print(output)


