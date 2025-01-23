input = open('day1/inp.txt').read().split('\n')

out = 0
for i in input:
    out += (int(i) // 3) -2

print(out)