inp = open('day11/inp.txt').read()

regi = {}
for ind, i in enumerate(inp.split(",")):
    regi[ind] = int(i)

def run(r, p, b, i):
    inputs = i.copy()
    pointer = p
    base = b
    register = r.copy()

    while not register[pointer] == 99:
        raw_instr = register[pointer]

        param_modes = [int(i) for i in list(("0"*(3-len(str(raw_instr//100)))) + str(raw_instr//100))]
        param_modes.reverse()
        instruction = raw_instr%100

        params = []
        for i in range(len(param_modes)):
            match param_modes[i]:
                case 0:
                    if pointer + i + 1 not in register:
                        register[pointer + i + 1] = 0
                    if register[pointer + i + 1] not in register:
                        register[register[pointer + i + 1]] = 0

                    params.append(register[pointer + i + 1])

                case 1:
                    if pointer + i + 1 not in register:
                        register[pointer + i + 1] = 0

                    params.append(pointer + i + 1)

                case 2:
                    if pointer + i + 1 not in register:
                        register[pointer + i + 1] = 0
                    if register[pointer + i + 1] + base not in register:
                        register[register[pointer + i + 1] + base] = 0

                    params.append(register[pointer + i + 1] + base)

        match instruction:
            #add first two params, store into third
            case 1:
                register[params[2]] = register[params[0]] + register[params[1]]
                pointer+=4
            
            #mult first two params, store into third
            case 2:
                register[params[2]] = register[params[0]] * register[params[1]]
                pointer+=4

            #input put into position
            case 3:
                register[params[0]] = inputs[0]
                inputs.pop(0)
                pointer+=2

            #output positon
            case 4:
                pointer+=2
                return (register[params[0]], register, pointer, base)

            #jump if true:
            case 5:
                if not register[params[0]] == 0:
                    pointer = register[params[1]]
                else:
                    pointer+=3
            
            #jump if not true:
            case 6:
                if register[params[0]] == 0:
                    pointer = register[params[1]]
                else:
                    pointer+=3

            #less than
            case 7:
                if register[params[0]] < register[params[1]]:
                    register[params[2]] = 1
                else:
                    register[params[2]] = 0
                pointer+=4
                
            
            #equals
            case 8:
                if register[params[0]] == register[params[1]]:
                    register[params[2]] = 1
                else:
                    register[params[2]] = 0
                pointer+=4
            
            #change base
            case 9:
                base += register[params[0]]
                pointer+=2
    return (-1,-1,-1,-1)

currPos = 0+0j
d = 1+0j
white = set()
painted = set()
state = [regi, 0, 0]

def map():
    for y in range(5, -5, -1):
        out = ""
        for x in range(-5, 5):
            if complex(y, x) in white:
                out+="#"
            elif complex(y,x) == currPos:
                match d:
                    case 1+0j:
                        out+="^"
                    case -1+0j:
                        out+="v"
                    case 0+1j:
                        out+=">"
                    case 0-1j:
                        out+="<"
            else:
                out+="."
        print(out)
    print()

while True:

    paint, state[0], state[1], state[2] = run(state[0], state[1], state[2], [1 if currPos in white else 0])

    if paint == -1:
        break
    elif paint == 1:
        white.add(currPos)
        painted.add(currPos)
    elif currPos in white:
        white.remove(currPos)
    
    rotate, state[0], state[1], state[2] = run(state[0], state[1], state[2], [1 if currPos in white else 0])

    if rotate == -1:
        break
    elif rotate:
        d *= 1j
    else:
        d *= -1j

    currPos+=d


print(len(painted))
print(len(white))
