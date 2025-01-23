input = open('day2/inp.txt').read().split('\n')

register = [int(i) for i in input[0].split(",")]
ogR = register.copy()
pointer = 0

for n in range(100):
    for v in range(100):
        register = ogR.copy()
        pointer = 0
        register[1] = n
        register[2] = v
        while not register[pointer] == 99:
            match register[pointer]:
                case 1:
                    instr = register[pointer:pointer+4]
                    register[instr[3]] = register[instr[1]] + register[instr[2]]
                case 2:
                    instr = register[pointer:pointer+4]
                    register[instr[3]] = register[instr[1]] * register[instr[2]]
            pointer+=4
        if register[0] == 19690720:
            print(100 * n + v)
            break
    if register[0] == 19690720:
        break
