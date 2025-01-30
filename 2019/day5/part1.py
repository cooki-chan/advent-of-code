import time


inp = open('day5/inp.txt').read().split('\n')

register = [int(i) for i in inp[0].split(",")]
pointer = 0

while not register[pointer] == 99:
    raw_instr = register[pointer]

    param_modes = [int(i) for i in list(("0"*(3-len(str(raw_instr//100)))) + str(raw_instr//100))]
    param_modes.reverse()
    instruction = raw_instr%100

    params = []
    for i in range(len(param_modes)):
        match param_modes[i]:
            case 0:
                params.append(register[pointer + i + 1])
            case 1:
                params.append(pointer + i + 1)
    

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
    # print(param_modes)
    # print(params)
    #print(register)
    print(instruction)
    #time.sleep(0.5)
    #print()
