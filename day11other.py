def stonify(stone, num):
    if num == 0:
        return 2 - int(len(str(stone)) % 2)
    
    if stone == 0:
        return stonify(1, num-1)
    elif len(str(stone)) % 2 == 0:
        half = int(len(str(stone)) / 2)
        return stonify(int(str(stone)[half::]), num-1) + stonify(int(str(stone)[:half:]), num-1)
    else:
        return stonify(stone*2024, num-1)

with open("day11input.txt", "r") as input:
    stones = [int(stone) for stone in input.readlines()[0].strip().split(" ")]
    
    blinks = 50
    
    total = 0
    i = 0
    for stone in stones:
        i += 1
        print(f"stone {i} started")
        total += stonify(stone, blinks-1)
        print(f"stone {i} calculated")
    
    print(f"There are {total} stones after {blinks} blinks")
