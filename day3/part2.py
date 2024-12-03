input = open('day3/inp.txt').read()

input = input.split("mul(")
for n, i in enumerate(input):
    if "do()" in i:
        input.insert(n+1, "do)")
    if "don't()" in i:
        input.insert(n+1, "dont)")

for n, i in enumerate(input):
    if ")" in input[n]:
        input[n] = i.split(")")[0]
    else:
        input[n] = " "

out = 0
add = True
for i in input:
    temp=i.split(",")
    if temp[0] == "do":
        add = True
    if temp[0] == "dont":
        add = False
    
    try:
        if add:
            if not " " in temp[0] and not " " in temp[1] and not "\n" in temp[0] and not "\n" in temp[1]:
                if int(temp[0]) < 1000 and int(temp[0]) < 1000:
                    out += int(temp[0]) * int(temp[1])
                    print(f"{int(temp[0]) * int(temp[1])} | {temp}")
    except:
        pass
        #print(temp)


print(out)