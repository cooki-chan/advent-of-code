input = open('11/inp.txt').read().split('\n')

adj = {}
for i in input:
    adj[i[0:i.index(":")]] = i[i.index(":")+2:].split(" ")

def find(start, end):
    dupes = {start:1, end:0}

    old = dupes.copy()
    old[end] = -1
    while dupes != old:
        seen = set()
        q = [start]
        while q != []:
            n = q.pop(0)
            pot = [i for i in adj[n] if i not in seen and (i != 'out' or end == 'out')]
            for i in pot:
                #print(i)
                if i not in q and i != end:
                    q += [i]
                    dupes[i] = 0
                dupes[i]+=dupes[n]
            q.sort(key=lambda x: dupes[x], reverse = True)
            seen.add(n)
        
        print(len(seen), len(adj.keys()))
    
    return dupes[end]

print(find('you', 'out'))


# print(find('svr','fft'), find('fft','dac'), find('dac','out'))
# print(find('svr','dac'), find('dac','fft'), find('fft','out'))