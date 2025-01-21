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
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            test1 = arr[i][j] + arr[i+1][j+1]+arr[i+2][j+2]
            test2 = arr[i][j+2] + arr[i+1][j+1]+arr[i+2][j+0]

            if test1 == "SAM" or test1 == "MAS":
                if test2 == "MAS" or test2 == "SAM":
                    out+=1

    return out

out = 0
out += check_diag(input)

print(out)
