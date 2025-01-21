def check(array):
    fail = False
    inc = array[0] - array[1] > 0
    for num, j in enumerate(array):
        if num+1 == len(array):
            continue
        if abs(array[num+1] - j) > 3 or abs(array[num+1] - j) == 0:
            fail = True
        elif (j - array[num+1] < 0 and inc) or (j - array[num+1] > 0 and not inc):
            fail = True
    return fail

input = open('day2/inp.txt').read().split('\n')

arr = []

for i in input:
    arr.append([int(item) for item in i.split()])

err = []
for n, i in enumerate(arr):
    err.append(i)
    for num, _ in enumerate(i):
        err[n][num] = 0

arr = []
input = open('day2/inp.txt').read().split('\n')
for i in input:
    arr.append([int(item) for item in i.split()])


count = 0
for n, i in enumerate(arr):
    if check(i):
        fail = 0
        for num, _ in enumerate(i):
            temp = i.copy()
            temp.pop(num)
            if check(temp):
                fail+=1
        if fail <= len(i)-1:
            count+=1
        print(fail)
        print(i)
    else:
        count+=1



print(count)
