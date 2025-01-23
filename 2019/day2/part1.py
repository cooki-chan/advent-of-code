input = open('day2/inp.txt').read().split('\n')

register = [int(i) for i in input[0].split(",")]
pointer = 0

register[1] = 12
register[2] = 2
while not register[pointer] == 99:
    match register[pointer]:
        case 1:
            instr = register[pointer:pointer+4]
            register[instr[3]] = register[instr[1]] + register[instr[2]]
        case 2:
            instr = register[pointer:pointer+4]
            register[instr[3]] = register[instr[1]] * register[instr[2]]
    pointer+=4

print(register[0])