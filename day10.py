def trailends(r, c, map):
    if map[r][c] == "9":
        return [(r, c)]
    
    ends = []

    n = int(map[r][c])
    for y, x in [(1,0),(-1,0),(0,1),(0,-1)]:
        R = r + y
        C = c + x
        if 0 <= R < len(map) and 0 <= C < len(map[0]) and int(map[R][C]) == n + 1:
            ends += [end for end in trailends(R, C, map) if end not in ends]
    return ends


with open("day10input.txt", "r") as input:
    map = [line.strip() for line in input.readlines()]

    total = 0

    for r in range(len(map)):
        for c in range(len(map)):
            if map[r][c] == "0":
                print(trailends(r,c,map))
                total += len(trailends(r, c, map))

    print(total)