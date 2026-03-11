input = open('06/inp.txt').read().split('\n')

DEPTH = 4
out = 0

nums = []
op = ""

for i in range(len(input[0])):
    if input[DEPTH][i] != " ":
        op = input[DEPTH][i]

    if str([input[k][i] for k in range(DEPTH)]) != str([" "] * DEPTH):
        bul = "".join([input[k][i] for k in range(DEPTH)])
        nums.append(int(bul))
    else:

        if op == "*":
            s = 1
            for u in nums:
                s *= u
            out += s

        elif op == "+":
            s = 0
            for u in nums:
                s += u
            out += s

        else:
            assert 0 == 1
        nums = []

print(out)
