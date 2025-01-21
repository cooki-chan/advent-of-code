i = open('day1/inp.txt')
input = i.readlines()

sum = 0
num_reference = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
for i in input:
    number = ""
    word = ""
    for j in i:
        for k in num_reference.keys():
            if k in word:
                number += num_reference[k]
                word = k[len(k)-1]
        if j.isdigit():
            number += j
        word += j

    if len(number) >= 2:
        number = number[0] + number[len(number)-1]
    else:
        number = number[0] + number[0]
    sum += int(number)
    print(f"{number} | {i} = {sum}")

print(sum)