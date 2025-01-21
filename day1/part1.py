input = ""
with open('day1/inp.txt') as i:
    input = i.readlines()

sum = 0
for i in input:
    number = ""
    for j in i:
        if j.isdigit():
            number += j
    if len(number) >= 2:
        number = number[0] + number[len(number)-1]
    else:
        number = number[0] + number[0]
    sum += int(number)

print(sum)