def isSafe(nums):
    dist = nums[0] - nums[1]

    if dist == 0 or abs(dist) > 3:
        return False

    sign = lambda dist : dist / abs(dist)
    lineSign = sign(dist)

    for i in range(2, len(nums)):
        dst = nums[i - 1] - nums[i]
        if dst == 0 or abs(dst) > 3 or sign(dst) != lineSign:
            return False
    
    return True

def problemDampener(nums):
    for i in range(len(nums)):
        s1 = []
        s2 = []
        try: s1 = nums[0::i]
        except: pass
        try: s2 = nums[i+1::]
        except: pass
        if isSafe(s1 + s2):
            return True
    return False

with open("day2/input.txt", "r") as input:
    safeCount = 0
    for line in input:
        nums = [int(n) for n in line.split(" ")]
        if isSafe(nums):
            print("safe")
            safeCount += 1
        elif problemDampener(nums):
            print("safe (dampened)")
            safeCount += 1
        else:
            print("unsafe")


    print(safeCount)