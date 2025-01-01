print("AAA".count("AAA"))

As = 0
rep3 = "AAA"
for ind in range(len(rep3)-1):
    if rep3[ind] == "A" and rep3[ind+1] == "A":
        As+=1
print(As)