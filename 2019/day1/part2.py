input = open('day1/inp.txt').read().split('\n')

def calc(val):
    out = 0
    while val > 0 and (int(val) // 3) -2 > 0:
        out += (int(val) // 3) -2
        val = (int(val) // 3) -2
    return out

out = 0
for i in input:
    out +=calc(int(i))

print(out)