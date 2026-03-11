input = open('11/inp.txt').read().split('\n')

adj = {}
for i in input:
    adj[i[0:i.index(":")]] = i[i.index(":")+2:].split(" ")

q = ["you"]
seen = []
seenout = 0

while q != []:
    print(q)
    n = q.pop(0)
    if n == "out":
        print(q.count('out'))
        break
    pot = [i for i in adj[n] if i not in seen]
    q += pot
    seen.append(n)

print(seenout)

# input = open('11/inp.txt').read().split('\n')

# adj = {}
# for i in input:
#     adj[i[0:i.index(":")]] = i[i.index(":")+2:].split(" ")

# def find(start, end):
#     q = [start]
#     seen = set()

#     while q != []:
#         print(len(seen))
#         n = q.pop(0)
#         if n == end:
#             return q.count(end)
#             continue
#         pot = [i for i in adj[n] if i not in seen and (i != 'out' or end == 'out')]
#         q += pot
#         seen.add(n)


# print(find('svr','fft'), find('fft','dac'), find('dac','out'))
# print(find('svr','dac'), find('dac','fft'), find('fft','out'))