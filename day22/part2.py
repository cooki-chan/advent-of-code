input = open('day22/inp.txt').read().split('\n')

input = [int(i) for i in input]

def mix(secret, mixed):
    return secret ^ mixed

def prune(secret):
    return secret % 16777216

def iter(secret, iter):
    out = secret
    out2 = []
    for _ in range(iter):
        out2.append(int(str(out)[-1]))
        temp = out
        temp = prune(mix(temp, temp * 64))
        temp = prune(mix(temp, temp // 32))
        temp = prune(mix(temp, temp * 2048))
        out = temp
    return out2

def calcChanges(prices):
    out = []
    for i in range(len(prices)-1):
        out.append(prices[i+1] - prices[i])
    return out

maxes = []
for i in input:
    max = {}
    prices = iter(i, 2000)
    changes = calcChanges(prices)
    for index, j in enumerate(prices):
        if index >= 4:
                        #past -> present
            code = (changes[index-4], changes[index-3], changes[index-2], changes[index-1])
            if not code in max.keys():
                max[code] = prices[index]
    maxes.append(max)

allCodes = set()
for i in maxes:
    for j in i.keys():
        allCodes.add(j)

max = 0
debug = []
k = ()
for i in allCodes:
    curr = 0
    d = []
    for j in maxes:
        if i in j.keys():
            curr += j[i]
            d.append(j[i])
    if curr > max:
        max = curr
        debug = d
        k = i
        print(i)
        print(curr)
print(max)
print(debug)
print(k)

