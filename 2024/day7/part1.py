input = open('day7/inp.txt').read().split('\n')

out = 0
for i in input:
    sol = int(i.split(":")[0])
    nums = [int(item) for item in i.split(":")[1].split()]
    print(f"{sol} | {nums}")

    poss = [nums[0]]
    nums.remove(nums[0])
    for j in nums:
        temp = []
        for k in poss:
            temp.append(k + j)
            temp.append(k * j)
        poss = temp.copy()
    
    if sol in poss:
        out += sol
    


print(out)