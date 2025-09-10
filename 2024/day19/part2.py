import functools

input = open('day19/inp.txt').read().split("\n")

possible = input[0].split(", ")
towels = possible

@functools.cache
def search(setup):
    if setup == "":
        return 1

    totals = 0
    for i in towels:
        if i in setup[0:len(i)]:
            totals += search(setup[len(i):])
    return totals

result = 0
for i in input[2:]:
    result += search(i)

print(result)