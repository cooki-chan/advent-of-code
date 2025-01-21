input = ""
with open('day2/inp1.txt') as i:
    input = i.readlines()

#OPPPONENT a: rock, b: paper, c:sizzor
#PLAY x: rock, y:paper, z:sizzor

#W:6, D:3, L:0
#X:1, Y:2, Z:3
#            D       W      L           L       D      W            W      L      D
wins = {"A":{"X":4, "Y":8, "Z":3}, "B":{"X":1, "Y":5, "Z":9}, "C":{"X":7, "Y":2, "Z":6}}
score = 0
for i in input:
    score += wins[i[0]][i[2]]   

print(score)