inp = open('day13/inp.txt').read()

regi = {}
for ind, i in enumerate(inp.split(",")):
    regi[ind] = int(i)

#state = [register, pointer, base]
def run(state, i):
    inputs = i.copy()
    pointer = state[1]
    base = state[2]
    register = state[0].copy()

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
                #state = [register, pointer, base]
                return (register[params[0]], [register, pointer, base])

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
    return (-1,-1)

map = {}
for i in range(5):
    map[i] = set()

saved = 0
state = [regi, 0, 0]

while not saved == -1:
    try:
        x, state = run(state, [])
        y, state = run(state, [])
        t, state = run(state, [])
    except TypeError:
        break

    map[t].add((x,y))

print(len(map[2]))
print(map[3])

def screen(map):
    brc = max([max(map[i]) for i in map])
    for y in range(brc[1]+1):
        out = ""
        for x in range(brc[0]+1):
            for i in map:
                if (x,y) in map[i]:
                    if i:
                        out += str(i)
                    else:
                        out+="`"

        print(out)
screen(map)