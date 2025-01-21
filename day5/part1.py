input = open('day5/inp.txt').readlines()

seeds = input[0].split("seeds: ")[1].split(" ")
seeds[len(seeds)-1] = seeds[len(seeds)-1][:-1]


currSection = {}
recording = False
for i, content in enumerate(input):
    if "\n" in content:
        content = content[:-1]
    
    if content == "":
        recording = False
        for j, value in enumerate(seeds):
            for k in currSection.keys():
                if int(value) >= int(k) and int(value) <= int(k) + int(currSection[k][1]):
                    modifier = int(currSection[k][0]) - int(k)
                    print(f"{value} + {modifier}")
                    seeds[j] = str(int(value) + int(currSection[k][0]) - int(k))
                    break
        
        print(currSection)
        print(seeds)
        print("")
        currSection = {}

    if recording:
        content = content.split(" ")
        currSection[content[1]] = (content[0], content[2])

    if "map:" in content:
        recording = True

lowest  = 89472398406590436
for i in seeds:
    if int(i) < lowest:
        lowest = int(i)

print(lowest)

