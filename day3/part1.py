input = open('day3/inp.txt').read()

input = input.split("mul(")

for n, i in enumerate(input):
    if ")" in input[n]:
        input[n] = i.split(")")[0]
    else:
        input[n] = " "

out = 0
for i in input:
    temp=i.split(",")
    try:
        if not " " in temp[0] and not " " in temp[1] and not "\n" in temp[0] and not "\n" in temp[1]:
            if int(temp[0]) < 1000 and int(temp[0]) < 1000:
                out += int(temp[0]) * int(temp[1])
                print(f"{int(temp[0]) * int(temp[1])} | {temp}")
    except:
        pass
        #print(temp)


print(out)