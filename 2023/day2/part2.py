i = open('day2/inp.txt')
input = i.readlines()

output = 0
for i in input: #all games loop
    gameNo = int(i[5:i.index(":")])
    
    maxRed = 0
    maxBlue = 0
    maxGreen = 0

    game = i[i.index(":")+1:].split(";") 
    for j in game: #each Pull in game loop
        for k in j.split(","): #color per pull
            data = k.split(" ")
            if "red" in data[2]:
                if int(data[1]) > maxRed:
                    maxRed = int(data[1])
            if "blue" in data[2]:
                if int(data[1]) > maxBlue:
                    maxBlue = int(data[1])
            if "green" in data[2]:
                if int(data[1]) > maxGreen:
                    maxGreen = int(data[1])
    
    output += maxRed * maxBlue * maxGreen

    
print(output)
        