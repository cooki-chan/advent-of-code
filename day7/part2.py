#Execution time: 0.56919509 seconds
import timeit
input = open('day7/inp.txt').read().split('\n')

def code(): 
    out = 0
    for i in input:
        sol = int(i.split(":")[0])
        nums = [int(item) for item in i.split(":")[1].split()]
        #print(f"{sol} | {nums}")

        poss = [nums[0]]
        nums.remove(nums[0])
        for j in nums:
            temp = []
            for k in poss:
                temp.append(k + j)
                temp.append(k * j)
                temp.append(int(str(k) + str(j)))
            poss = temp.copy()
        
        if sol in poss:
            out += sol
    
    print(out)

execution_time = 0
for i in range(10):
    execution_time += timeit.timeit(code, number=1)
print(f"Execution time: {execution_time/10} seconds")