input = open('day1/inp.txt').read().split('\n')

left = []
right = {}

for i in input:
    left.append(int(i.split(" ")[0]))
    if not int(i.split(" ")[len(i.split(" "))-1]) in right.keys():
        right[int(i.split(" ")[len(i.split(" "))-1])] = 1
    else:
        right[int(i.split(" ")[len(i.split(" "))-1])] +=1

print(left)
print(right)

out = 0
for le in left:
    if not le in right.keys():
        continue
    out += le * right[le]

print(out)


