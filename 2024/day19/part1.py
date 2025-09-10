import functools

input = open('day19/inp.txt').read().split("\n")

possible = input[0].split(", ")
# possible.sort(key = len)

# cleaned = possible.copy()

# for i in possible:
#     cleaned = [j.replace(i, "") for j in cleaned]

# towels = []
# for ind, i in enumerate(cleaned):
#     if len(possible[ind]) == 1 or len(i) > 0:
#         towels.append(possible[ind])

# towels.reverse()
# print(towels)

towels = possible

@functools.cache
def search(setup):
    if setup == "":
        return True

    for i in towels:
        if i in setup[0:len(i)]:
            if search(setup[len(i):]):
                return True
    return False

result = 0
for i in input[2:]:
    if search(i):
        result +=1
        print(i)

print(result)