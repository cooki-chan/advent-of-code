input = ""
with open('day2/inp1.txt') as i:
    input = i.readlines()

#OPPPONENT a: rock, b: paper, c:sizzor
#RESULT x:L, y:D, z:W

#X:0, Y:3, Z:6
#ROK:1, PPR:2, SIZ:3

#            SIZ    ROK    PPR          ROK    PPR    SIZ          PPR    SIZ    ROK
wins = {"A":{"X":3, "Y":4, "Z":8}, "B":{"X":1, "Y":5, "Z":9}, "C":{"X":2, "Y":6, "Z":7}}
score = 0
for i in input:
    score += wins[i[0]][i[2]]   

print(score)