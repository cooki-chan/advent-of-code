input = open('day5/inp2.txt').readlines()

rawseeds = input[0].split("seeds: ")[1].split("  ")
seeds = []

for i in rawseeds:
    temp = i.split(" ")
    seeds.append((temp[0], str(int(temp[0]) + int(temp[1]))))
#idea: save seeds as range from first to last
#use range math to apply the things, and just create new tuples when you compare to a new range. 
#from there, you can find the lowest numbers within the ranges when done

# input = (output, range)
currSection = {}
recording = False
for i, content in enumerate(input):
    if "\n" in content:
        content = content[:-1]
    
    #if encounter \n, do the math b/c end section
    if content == "":
        recording = False
        newSeeds = []
        print(str(currSection))

        for j, value in enumerate(seeds):
            outSeed = []
            for k in currSection.keys():
                if int(k) < int(value[1]) and int(k) >= int(value[0]) and int(value[1]) > int(k) + int(currSection[k][1]): #check if left bound of seed range fits but right doesnt
                    newSeedStart = str(int(value[0]) + int(currSection[k][0]) - int(k)) #range applies to beginning
                    newSeedEnd = str(int(currSection[k][0]))
                    outSeed.append((newSeedStart, newSeedEnd))

                    newSeedStart = str(k) #range doesnt apply to end
                    newSeedEnd = str(int(value[1]))
                    outSeed.append((newSeedStart, newSeedEnd))

                if int(value[0]) < int(k) and int(value[1]) >= int(k) and int(value[1]) < int(k) + int(currSection[k][1]): #check if right bound fits but left doesnt
                    newSeedStart = str(int(value[0])) #range doent apply to beginning
                    newSeedEnd = str(int(k)-1)
                    newSeeds.append((newSeedStart, newSeedEnd))

                    newSeedStart = str(currSection[k][0]) #range applies to end
                    newSeedEnd = str(int(currSection[k][0]) + int(currSection[k][0]) - int(k))
                    newSeeds.append((newSeedStart, newSeedEnd))
                
                if int(value[0]) > int(k) and int(value[1]) < int(k) + int(currSection[k][1]):
                    newSeedStart = str(int(value[0]) + int(currSection[k][0]) - int(k)) #range applies to end
                    newSeedEnd = str(int(value[1]) + int(currSection[k][0]) - int(k))
                    newSeeds.append((newSeedStart, newSeedEnd))

            if outSeed == []:
                newSeeds.append(value)
            else:
                for k in outSeed:
                    newSeeds.append(k)
                
                
        seeds = newSeeds
        print(str(seeds) + "\n")



        
        currSection = {}

    #record info
    if recording:
        content = content.split(" ")
        currSection[content[1]] = (content[0], content[2])

    #start recording
    if "map:" in content:
        recording = True




lowest  = int(seeds[0][0])
for i in seeds:
    if int(i[0]) < lowest:
        lowest = int(i[0])
print(lowest)
