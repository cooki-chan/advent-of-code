inp = open('day7/inp.txt').read().split('\n')

def compute(input):
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
                register[params[0]] = input[0]
                input.pop(0)
                pointer+=2

            #output positon
            case 4:
                return register[params[0]]
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

peak = 0
peak_index = 0

curr = 1234

while curr < 43211:
    print(curr)
    fail = False
    if not len(set(list(str(curr)))) == len(str(curr)):
        curr+=1
        continue
    for i in str(curr):
        if i in "56789":
            fail = True
            break
    if fail:
        curr+=1
        continue
    

    saved = 0
    for i in range(5):
        saved = compute([int(("0" * (5-len(str(curr))) + str(curr))[i]), saved])
        #print("a")
    if saved > peak:
        peak = saved
        peak_index = curr
        #print(peak)
    curr+=1
print()
print(peak, peak_index)