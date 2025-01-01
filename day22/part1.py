input = open('day22/inp.txt').read().split('\n')

input = [int(i) for i in input]

def mix(secret, mixed):
    return secret ^ mixed

def prune(secret):
    return secret % 16777216

def iter(secret, iter):
    out = secret
    for _ in range(iter):
        temp = out
        temp = prune(mix(temp, temp * 64))
        temp = prune(mix(temp, temp // 32))
        temp = prune(mix(temp, temp * 2048))
        out = temp
    return out


sum = 0
for i in input:
    sum += iter(i, 2000)
print(sum)