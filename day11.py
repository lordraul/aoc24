with open("day11input.txt", "r") as input:
    stones = [int(stone) for stone in input.readlines()[0].strip().split(" ")]
    
    for blink in range(75):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                stone = str(stones[i])
                half = int(len(stone) / 2)
                stones[i] = int(stone[half::])
                stones.insert(i, int(stone[:half:]))
                i += 1
            else:
                stones[i] *= 2024
            i += 1
        print(f"blink{blink} complete")
    print(f"There are {len(stones)} stones after {blink+1} blinks")