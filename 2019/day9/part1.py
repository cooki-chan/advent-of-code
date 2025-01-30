inp = open('day9/inp.txt').read()

register = {}
for ind, i in enumerate(inp.split(",")):
    register[ind] = int(i)

pointer = 0
base = 0

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
            register[params[0]] = int(input("what: "))
            pointer+=2

        #output positon
        case 4:
            print(register[params[0]], "FROM 4")
            pointer+=2

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
