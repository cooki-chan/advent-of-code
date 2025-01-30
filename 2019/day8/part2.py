input = open('day8/inp.txt').read()

width = 25
height = 6

rows = []
while not input == "":
    rows.append(input[0:width])
    input = input[width:]

layers = []
while not rows == []:
    layers.append("".join(rows[0:height]))
    rows = rows[height:]

out = ""
for i in range(len(layers[0])):
    layer = 0
    while layers[layer][i] == "2":
        layer+=1
    out+=layers[layer][i]

out = out.replace("0", " ")
out = out.replace("1", "8")

while not out == "":
    print(out[:width])
    out = out[width:]
print(out)

