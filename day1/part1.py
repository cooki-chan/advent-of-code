input = open('day1/inp.txt').read().split('\n')

left = []
right = []

for i in input:
    left.append(int(i.split(" ")[0]))
    right.append(int(i.split(" ")[len(i.split(" "))-1]))

left.sort()
right.sort()

print(left)
print(right)

t = 0
for num, l in enumerate(left):

    t += abs(l - right[num])

print(t)

