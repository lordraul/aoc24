with open("day2/input.txt", "r") as input:
    safeCount = 0
    for line in input:
        try:
            nums = [int(n) for n in line.split(" ")]
            dist = nums[0] - nums[1]

            if dist == 0 or abs(dist) > 3:
                print("Unsafe")
                continue

            sign = lambda dist : dist / abs(dist)
            lineSign = sign(dist)

            for i in range(2, len(nums)):
                dst = nums[i - 1] - nums[i]
                if dst == 0 or abs(dst) > 3 or sign(dst) != lineSign:
                    raise
            
            safeCount += 1
            print("Safe")
                
        except:
            print("Unsafe")
            pass

    print(safeCount)