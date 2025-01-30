inp = open('day7/inp.txt').read().split('\n')

def compute(input, reg, p):
    register = reg
    pointer = p

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
                register[params[0]] = input[0]
                input.pop(0)
                pointer+=2

            #output positon
            case 4:
                pointer+=2
                return (register[params[0]], register, pointer)

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
    return (-1, -1, -1)

peak = 0
peak_index = 0

curr = 56789

while curr < 98766:
    fail = False
    if not len(set(list(str(curr)))) == len(str(curr)):
        curr+=1
        continue
    for i in str(curr):
        if i in "01234":
            fail = True
            break
    if fail:
        curr+=1
        continue
    states = [[int(i) for i in inp[0].split(",")] for _ in range(5)]
    pointers = [0 for _ in range(5)]
    saved = 0
    for i in range(5):
        saved, states[i], pointers[i] = compute([int(("0" * (5-len(str(curr))) + str(curr))[i]), saved], states[i], pointers[i])
    while True:
        for i in range(5):
            saved, states[i], pointers[i] = compute([saved], states[i], pointers[i])
            #print("a")
            #print(saved)
            #print(pointers)
            if states[i] == -1:
                break
            print(curr, i)
        if saved == -1:
            break
        if saved > peak:
            print(curr)
            peak = saved
            peak_index = curr
    curr+=1
    print()
print()
print(peak, peak_index)