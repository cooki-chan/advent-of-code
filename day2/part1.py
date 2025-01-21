input = open('day2/inp.txt').read().split('\n')

arr = []

for i in input:
    arr.append([int(item) for item in i.split()])
    

count = 0
for i in arr:
    out = False
    inc = i[0] - i[1] > 0

    for num, j in enumerate(i): 
        if num+1 == len(i):
            continue
        if abs(i[num+1] - j) > 3 or abs(i[num+1] - j) == 0:
            out = True
        if (j - i[num+1] < 0 and inc) or (j - i[num+1] > 0 and not inc):
            out = True
    if not out:
        count+=1
        print(i)

print(count)
