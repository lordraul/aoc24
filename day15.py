def findEmptySpace(x, y, move, )

with open("day15input.txt", "r") as input:
    lines = [[c for c in line.strip()] for line in input.readlines()]
    room = [line for line in lines if "#" in line]

    robx = 0
    roby = lines.index([])
    
    instructions = ["^v<>".index(let) for line in lines for let in line if "^" in line]
    print(instructions)