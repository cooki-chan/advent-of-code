input = open('day6/inp.txt').readlines()

input[0] = input[0].split(":")[1].strip()
input[1] = input[1].split(":")[1].strip()

times = input[0].split(" ")
dists = input[1].split(" ")

leaderboard = {}
while "" in times:
    times.remove("")

while "" in dists:
    dists.remove("")

for i, value in enumerate(times):
    leaderboard[value] = dists[i]

output = 1
for time in leaderboard:
    out = 0
    for heldTime in range(int(time)):
        dist = (int(time) - heldTime) * heldTime
        if dist > int(leaderboard[time]):
            
            out +=1
    if not out == 0:
        output *= out

print(output)
