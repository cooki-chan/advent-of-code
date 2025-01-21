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
                seedLeft = int(value[0])
                seedRight = int(value[1])

                rangeLeft = int(k)
                rangeRight = int(k) + int(currSection[k][1])

                #encounter 1: both sides of seeds fits within section range
                if seedLeft >= rangeLeft and seedRight < rangeRight:
                #encounter 2: left side outside, right side inside
                if seedLeft < rangeLeft and seedRight < rangeRight:
                #encounter 3: left side inside, right side outside
                if seedLeft >= rangeLeft and seedRight > rangeRight:
                #encounter 4: both sides of seeds outside, but section range fits within seeds 
                if seedLeft < rangeLeft and seedRight > rangeRight:

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
    if int(i[0]) < lowest and int(i[0]) > 0:
        lowest = int(i[0])
print(lowest)
