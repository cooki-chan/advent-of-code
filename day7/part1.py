input = open('day7/inp.txt').readlines()

class hand:
    def __init__(self, hand, bet) -> None:
        self.hand = hand
        self.bet = bet
        pass

    def __lt__(self, other):
        values = "23456789TJQKA"
        for i, card in enumerate(self.hand):
            oppCard = other.hand[i]
            if values.index(card) > values.index(oppCard):
                return False
            elif values.index(card) < values.index(oppCard):
                return True
        return True
    
    def __str__(self):
        return f"[{self.hand}, {self.bet}]"

five = []
four = []
full = []
three = []
twoPair = []
onePair = []
highCard = []

for i, data in enumerate(input):
    data = data.split(" ")
    handStr = data[0]
    bet = data[1][:-1]

    handParsed = {}
    for j in handStr:
        if j in handParsed:
            handParsed[j]+=1
        else:
            handParsed[j]=1
    
    if 5 in handParsed.values():
        five.append(hand(handStr, int(bet)))
    elif 4 in handParsed.values():
        four.append(hand(handStr, int(bet)))
    elif 3 in handParsed.values() and 2 in handParsed.values():
        full.append(hand(handStr, int(bet)))
    elif len(handParsed.keys()) == 3 and 3 in handParsed.values():
        three.append(hand(handStr, int(bet)))
    elif len(handParsed.keys()) == 3 and 2 in handParsed.values():
        twoPair.append(hand(handStr, int(bet)))
    elif len(handParsed.keys()) == 4 and 2 in handParsed.values():
        onePair.append(hand(handStr, int(bet)))
    else:
        highCard.append(hand(handStr, int(bet)))

#weakest card will come first 
five.sort()
four.sort()
full.sort()
three.sort()
twoPair.sort()
onePair.sort()
highCard.sort()

output = 0
rank = 1
for i in highCard:
    output += i.bet * rank
    rank +=1
for i in onePair:
    output += i.bet * rank
    rank +=1
for i in twoPair:
    output += i.bet * rank
    rank +=1
for i in three:
    output += i.bet * rank
    rank +=1
for i in full:
    output += i.bet * rank
    rank +=1
for i in four:
    output += i.bet * rank
    rank +=1
for i in five:
    output += i.bet * rank
    rank +=1

print(output)

    
