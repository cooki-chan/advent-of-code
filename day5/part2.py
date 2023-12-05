input = open('day5/inp.txt').readlines()

rawseeds = input[0].split("seeds: ")[1].split("  ")
outputs = []



#idea: save seeds as range from first to last
#use range math to apply the things, and just create new tuples when you compare to a new range. 
#from there, you can find the lowest numbers within the ranges when done

print("auojihbgnsoueilj")
for i in rawseeds:
    seeds = []
    for j in range(int(i.split(" ")[1])):
        seeds.append(int(i.split(" ")[0])+j)

    currSection = {}
    recording = False
    for i, content in enumerate(input):
        if "\n" in content:
            content = content[:-1]
        
        if content == "":
            recording = False
            for j, value in enumerate(seeds):
                for k in currSection.keys():
                    print(j)
                    if int(value) >= int(k) and int(value) <= int(k) + int(currSection[k][1]):
                        modifier = int(currSection[k][0]) - int(k)
                        print(f"{value} + {modifier}")
                        seeds[j] = str(int(value) + int(currSection[k][0]) - int(k))
                        break
            
            currSection = {}

        if recording:
            content = content.split(" ")
            currSection[content[1]] = (content[0], content[2])

        if "map:" in content:
            recording = True
    
    lowest  = int(seeds[0])
    for i in seeds:
        if int(i) < lowest:
            lowest = int(i)
    print(lowest)
    outputs.append(lowest)



lowest  = int(outputs[0])
for i in outputs:
    print(i)
    if int(i) < lowest:
        lowest = int(i)
print(lowest)
