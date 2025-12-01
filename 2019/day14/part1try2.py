import math


input = open('day14/inp.txt').read().split('\n')

reactions = {"ORE":[[1, "ORE"], 1]}
oreConversions = {}

for i in input:
    r = i.split(" => ")
    if "ORE" not in r[0]:
        result = (int(r[1].split(" ")[0]), r[1].split(" ")[1])
        reactants = [[int(i.split(" ")[0]), i.split(" ")[1]] for i in r[0].split(", ")]
        reactions[result[1]] = [reactants, result[0]]
    else:
        result = (int(r[1].split(" ")[0]), r[1].split(" ")[1])
        reactants = [[int(i.split(" ")[0]), i.split(" ")[1]] for i in r[0].split(", ")]
        oreConversions[result[1]] = [reactants[0][0], result[0]]

