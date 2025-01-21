def build(rowIn):
    row = []
    for i in rowIn:
        row.append(int(i))
    chart = []
    newRow = []

    while sum(row) != 0:
        for i, num in enumerate(row):
            if i < len(row)-1:
                newRow.append(row[i+1] - row[i])
        chart.append(row)
        row = newRow
        newRow = []
    chart.append(row)
    return chart

def extrapolate(chartIn):
    currVal = 0
    for i in range(len(chartIn)-2, -1, -1):
        currVal = chartIn[i][0] - currVal
    return currVal



input = open('day9/inp.txt').read().split("\n")
out = 0
for position in input:
    chart = build(position.split(" "))
    out += extrapolate(chart)

print(out)


