input = open('day23/inp.txt').read().split('\n')

connections = {}

for i in input:
    one = i[:2]
    two = i[3:]

    if one in connections.keys():
        connections[one].append(two)
    else:
        connections[one] = [two]

    if two in connections.keys():
        connections[two].append(one)
    else:
        connections[two] = [one]

def check(current, added):
    # check if added fits into all the others
    options = set(connections[current[0]])
    for i in current: 
        options = options.intersection(connections[i])

    if added not in options:
        return False

    #check if all in current are in added
    for i in current:
        if i not in connections[added]:
            return False
    
    return True


largest = []
for i in connections:
    print(i)
    options = connections[i]
    currentOptions = [[i]]

    for j in options:
        for k in currentOptions:
            if check(k, j):
                currentOptions.append(k + [j])

    currentOptions.sort(key=len, reverse=True)
    if len(currentOptions[0]) > len(largest):
        largest = currentOptions[0]

largest.sort()
out = ""
for i in largest:
    out += i + ","
out = out[:-1]
print(out)

