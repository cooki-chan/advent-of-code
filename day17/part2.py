input = open('day17/inp.txt').read().split('\n')
A = int(input.pop(0).split(":")[1].strip())
B = int(input.pop(0).split(":")[1].strip())
C = int(input.pop(0).split(":")[1].strip())
input.pop(0)
input = [int(i) for i in input.pop(0).split(":")[1].strip().split(",")]

def calc(A):
    A = A
    B = 0
    C = 0
    out = ""
    currInstruction = 0
    while currInstruction < len(input):
        instr = input[currInstruction]
        lit = input[currInstruction+1]
        combo = 0

        if lit <= 3:
            combo = lit
        else:
            match lit:
                case 4:
                    combo = A
                case 5:
                    combo = B
                case 6:
                    combo = C
                case 7:
                    print("how the fuck")
        
        match instr:
            case 0:
                A = A // pow(2, combo)
            case 1:
                B = B ^ lit
            case 2:
                B = combo % 8
            case 3:
                if not A == 0:
                    currInstruction = lit - 2
            case 4:
                B = B ^ C
            case 5:
                out+=str(combo % 8) + ","
            case 6:
                B = A // pow(2, combo)
            case 7:
                C = A // pow(2, combo)

        currInstruction +=2
    out = [int(i) for i in out[0:len(out)-1].split(",")]
    return out

a = pow(8, len(input)-1) #hard coding
test = calc(pow(8,len(input)-1))
while not calc(a) == input:
    for i in range(len(input)-1, -1, -1): #digit check
        if not test[i] == input[i]:
            a+=pow(8, i)
            test = calc(a)
            break

print(test)
print(a)