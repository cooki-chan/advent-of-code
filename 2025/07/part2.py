# input = open('07/inp.txt').read().split('\n')
# #input = open('07/ex_inp.txt').read().split('\n')

# tls = [0] * len(input[0])
# tls[input[0].index("S")] = 1

# for i in input:
#     new = [0] * len(input[0])
#     for ind, j in enumerate(tls):
#         if i[ind] == "^":
#             new[ind-1] += tls[ind]
#             new[ind+1] += tls[ind]
#         else:
#             new[ind] += tls[ind]
#     tls = new

# print(sum(tls))


input = open('07/inp.txt').read().split('\n')
input = open('07/ex_inp.txt').read().split('\n')


tach = []
for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j == "^":
            tach.append((row, col))

q = [(0, input[0].index("S"))]
old = []
out = []

def rec(l):
    out = 1
    if l[0]+1 >= len(input):
        return out
    if (l[0]+1, l[1]) in tach:
        out += rec((l[0]+1, l[1]-1))
        out += rec((l[0]+1, l[1]+1))
    else:
        out += rec((l[0]+1, l[1]))
    return out

print(rec((0, input[0].index("S"))))

