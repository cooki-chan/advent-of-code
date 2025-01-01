input = open('day24/inp.txt').read().split('\n\n')
input[0] = input[0].split("\n")
input[1] = input[1].split("\n")

bits = {}
print(input)

for i in input[0]:
    bits[i.split(":")[0]] = int(i.split(":")[1])


while not input[1] == []:

    for i in input[1]:
        if "AND" in i:
            out = i.split(" -> ")[1]
            codes = i.split(" -> ")[0].split(" AND ")

            if codes[0] in bits.keys() and codes[1] in bits.keys():
                bits[out] = bits[codes[0]] and bits[codes[1]]
                input[1].remove(i)

        elif " OR " in i:
            out = i.split(" -> ")[1]
            codes = i.split(" -> ")[0].split(" OR ")

            if codes[0] in bits.keys() and codes[1] in bits.keys():
                bits[out] = bits[codes[0]] or bits[codes[1]]
                input[1].remove(i)
        
        elif " XOR " in i:
            out = i.split(" -> ")[1]
            codes = i.split(" -> ")[0].split(" XOR ")

            if codes[0] in bits.keys() and codes[1] in bits.keys():
                bits[out] = bits[codes[0]] ^ bits[codes[1]]
                input[1].remove(i)


out = 0
for i in range(100):
    if "z" + "{:02d}".format(i) in bits.keys():
        out += pow(2, i) * int(bits["z" + "{:02d}".format(i)])

print(out)