def findEmptySpace(x, y, move, room):
    if room[y][x] == "#":
        return (-1,-1)
        
    x += (move > 1) * (-1 if move % 2 == 0 else 1)
    y += (move < 2) * (-1 if move % 2 == 0 else 1)
    
    if room[y][x] == ".":
        return (x,y)
    
    return findEmptySpace(x, y, move, room)

with open("day15input.txt", "r") as input:
    lines = [[c for c in line.strip()] for line in input.readlines()]
    room = [line for line in lines if "#" in line]

    roby = lines.index([line for line in room if "@" in line][0])
    robx = room[roby].index("@")
    
    instructions = ["^v<>".index(let) for line in lines for let in line if "^" in line]
    for instruction in instructions:
        x, y = findEmptySpace(robx, roby, instruction, room)
        if x >= 0:
            nextx = robx + (instruction > 1) * (-1 if instruction % 2 == 0 else 1)
            nexty = roby + (instruction < 2) * (-1 if instruction % 2 == 0 else 1)
            
            if room[nexty][nextx] == "O":
                room[y][x] = "O"
            
            room[roby][robx] = "."
            robx, roby = nextx, nexty
            room[roby][robx] = "@"
            
    gps = 0
    
    for y in range(len(room)):
        for x in range(len(room[0])):
            if room[y][x] == "O":
                gps += 100 * y + x
                
    print(f"GPS Sum is {gps}")
