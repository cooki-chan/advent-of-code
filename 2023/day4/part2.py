i = open('day4/inp.txt')
input = i.readlines()

for i in range(len(input)):
    input[i] = input[i].split(":")[1]

noCards = len(input)
cardsList = [1] * len(input)

for i in range(len(input)):
    parsed = input[i].split("| ")
    winningNums = parsed[0]
    losingNums = parsed[1]

    cardsWon = 0
    for j in losingNums.split(" "):
        if "\n" in j:
            j = j[0:len(j)-1]

        if " "+j+" " in winningNums and not j == "":
            cardsWon+=1
    
    for j in range(cardsWon):
        if j+i+1 < len(input):
            cardsList[j+i+1] = cardsList[j+i+1] + cardsList[i]
            noCards+=cardsList[i]
    
print(noCards)

