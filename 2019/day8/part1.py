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

z = 100
out = 0
for i in layers:
    c = i.count("0")
    if c < z:
        z = c
        out = i.count("1")* i.count("2")

print(out)
