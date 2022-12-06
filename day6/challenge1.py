input = ""
with open('day6/inp1.txt') as i:
    input = i.readline()
    input = input.replace("\n", "") 

markerStr = ""
firstInstance = -1
for i in range(len(input)-1):

    if len(markerStr) == 4:
        markerStr = markerStr[1:4] + input[i]
        
        works = True
        for j in markerStr:
            testStr = markerStr.replace(j, "", 1)
            print(testStr)
            if j in testStr:
                works = False
        
        if works:
            print(i)
            if firstInstance == -1:
                firstInstance = i
    else:
        markerStr += input[i]

print(firstInstance + 1)


