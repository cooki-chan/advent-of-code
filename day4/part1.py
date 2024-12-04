input = open('day4/inp.txt').read().split("\n")

def rotate(arr):
    out = []
    for j in range(len(arr)):
        out.append("")

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            out[j] += arr[i][j]
    return out

def check_diag(arr):
    out = 0
    for i in range(len(arr)-3):
        for j in range(len(arr[0])-3):
            test1 = arr[i][j] + arr[i+1][j+1]+arr[i+2][j+2]+arr[i+3][j+3]
            test2 = arr[i][j+3] + arr[i+1][j+2]+arr[i+2][j+1]+arr[i+3][j]

            if test1 == "XMAS" or test1 == "SAMX":
                out+=1

            if test2 == "XMAS" or test2 == "SAMX":
                out+=1
    return out

out = 0
for i in input:
    out += i.count("XMAS")
    out += i.count("SAMX")
input = rotate(input)

for i in input:
    out += i.count("XMAS")
    out += i.count("SAMX")
input = rotate(input)

out += check_diag(input)

print(out)
