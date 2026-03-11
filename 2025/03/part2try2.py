input = open('03/inp.txt').read().split('\n')

itr = 12
out = 0

for i in input:
    frame = i[0:len(i)-(itr-1)]
    left = i[len(i)-(itr-1):]
    num = ""

    for _ in range(itr):
        added = max(list(frame))
        frame = frame[frame.index(added)+1:]
        if(len(left) > 0):
            frame += left[0]
        left = left[1:]
        num += added

    out += int(num)
    print(num)


print(out)