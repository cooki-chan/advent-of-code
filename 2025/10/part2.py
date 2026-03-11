import numpy
import itertools

input = open('10/inp.txt').read().split('\n')

input = [i.split(" ") for i in input]
result = []

for ind, i in enumerate(input):
    new = []
    for j in i:
        if '(' in j:
            s = j[1:len(j)-1].split(",")
            out = [0] * (i[-1].count(",") + 1)
            for k in s:
                out[int(k)] = float(1)
            new.append(out)

        if '{' in j:
            s = j[1:len(j)-1]
            out = [float(i) for i in s.split(",")]
            result.append(out)

    input[ind] = new

def subtract(base, operand):
    out = []
    for ind, i in enumerate(base):
        out.append(i - operand[ind])
    return out

out = []

for ind, _ in enumerate(input):

    matrix = input[ind]
    matrix.append(result[ind])
    matrix = numpy.array(matrix)
    matrix = numpy.rot90(matrix)
    matrix = numpy.flip(matrix, axis= 0)

    print()

    row = 0
    for col in range(len(matrix[0])):
        print(matrix)
        print()
        #print(col, ind)
        #print(matrix)

        #if pivot value is 0
        if matrix[row][col] == 0:
            for i in range(row+1, len(matrix)):
                if matrix[i][col]!= 0:
                    temp = matrix[i].copy()
                    matrix[i] = matrix[row]
                    matrix[row] = temp
                    break
            
            #if still 0, this is an empty column. skip
            if matrix[row][col] == 0:
                continue
        
        #working down
        for i in range(row+1, len(matrix)):
            matrix[i] = subtract(matrix[i], (matrix[row] * matrix[i][col]) / matrix[row][col])
        
        
        
        row+=1

        if row >= len(matrix):
            break

    # remove blank rows
    matrix = matrix.tolist()
    while [0] * len(matrix[0]) in matrix:
        matrix.remove([0] * len(matrix[0]))
    matrix = numpy.array(matrix)

    print(matrix)

    #make diagonal 1s:
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j != 0:
                matrix[i] = matrix[i] / j
                break

    #go back up
    for i in range(len(matrix)-1, 0, -1):
        pivot = -1
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                pivot = j
                break
        
        for j in range(i):
            matrix[j] = subtract(matrix[j], (matrix[i] * matrix[j][pivot]) / matrix[i][pivot])
        



    print(numpy.array(matrix))
    print()
    matrix = numpy.rot90(matrix, 3)
    free = []
    for i in matrix:
        for j in i:
            if i.tolist() != [0] * len(i) and j != 0 and j != 1:
                free.append(i)
                break
    
    out.append(free)

print(out)

DEBUX = 1

# def find_lowest(info):
#     presses = info[-1]
#     buttons = info[:-1]


#     lowest = 10000000
#     ind = 1
#     extra_search = 10
#     seen = set()
#     while lowest == 10000000 or extra_search != 0:
#         print(ind)
#         combos = itertools.product(range(ind), repeat = len(buttons))
#         for i in combos:
#             if i in seen:
#                 continue
#             seen.add(i)

#             change = numpy.array(buttons[0] * 0)

#             for dex, j in enumerate(i):
#                 change += buttons[dex] * j
#                 # print(change, buttons[dex], buttons[dex] * j, i)

#             test = presses - change
#             a = sum(test) + sum(i)
#             if min(test) >= 0 and a < lowest:
#                 int_test = True
#                 for j in test:
#                     if j - int(j) > 0.01:
#                         int_test = False
#                         # print("INT FAIL")
#                         # print(sum(test), test, i)
#                         break
#                 if int_test:
#                     lowest = a
#                     print(i, test, a, "WAH WAH WAH")
#             if ind == 2000:
#                 print(matrix)
#                 print(DEBUX)
#                 print(test, a)
#                 print(presses, change)
#                 print(buttons)
#                 assert 0 == 1
#                     # print(sum(test), test, i)
#             # print(test)
#             # print()


#         ind+=1
#         if lowest != 10000000:
#             extra_search-=1

        


#     return int(lowest)

def find_lowest(info):
    presses = info[-1]
    buttons = info[:-1]

    limits = [10000] * len(buttons)

    for ind, press in enumerate(presses):
        pass


please = 0

for loading, i in enumerate(out):
    added = 0
    print(loading, "AAAAAAAAAAAAAAAAAAAAA")
    if len(i) > 1:
        added += numpy.sum(find_lowest(i)).item()
    else:
        added += numpy.sum(i).item()
    print(added, i)
    please += added
    DEBUX +=1

print(please)
