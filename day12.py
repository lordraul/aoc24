def printRegion(region, garden):
    for r in range(len(garden)):
        line = ""
        for c in range(len(garden[0])):
            if (r,c) in region:
                line += "\033[95m"
            line += garden[r][c] + "\033[0m"
        print(line)
            
def findRegion(r, c, plant, garden):
    plants = []
    
    for R, C in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if 0 <= R < len(garden) and 0 <= C < len(garden[0]):
            if garden[R][C] == plant:
                plants += [(R,C)]
                garden[R][C] = "."
    
    region = [(r,c)]
    
    for R, C in plants:
        region += findRegion(R, C, plant, garden)

    return region

def countSides(region, garden):
    edges = []
    edgeTypes = []
    sides = 0

    for r, c in region:
        touches = [(R,C) for R, C in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)] if (R, C) in region]
        if len(touches) < 4:
            edges += [(r,c)]
            edgeTypes += [sum([pow(2, [(r+1,c),(r-1,c),(r,c+1),(r,c-1)].index((R,C))) for R,C in touches])]
            sides += 4 - len(touches)
    
    for r in range(1, len(garden)):
        for c in range(len(garden[0])):
            printRegion([(r,c),(r-1,c)], garden)
            if (r,c) in edges and (r-1,c) in edges:
                sides -= edgeTypes[edges.index((r,c))] & edgeTypes[edges.index((r-1,c))]

    for r in range(len(garden)):
        for c in range(1, len(garden[0])):
            printRegion([(r,c),(r,c-1)], garden)
            if (r,c) in edges and (r,c-1) in edges:
                sides -= edgeTypes[edges.index((r,c))] & edgeTypes[edges.index((r,c-1))]

    return sides


with open("day12input.txt", "r") as input:
    lines = input.readlines()
    garden = [[plant for plant in line.strip()] for line in lines]
    
    checked = []
    regions = []
    
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r, c) not in checked:
                region = list(set(findRegion(r, c, garden[r][c], garden)))
                regions += [region]
                checked += region

    garden = [[plant for plant in line.strip()] for line in lines]
    
    total = 0
    discountTotal = 0

    for region in regions:
        area = len(region)
        perm = 4 * area
        for r, c in region:
            for R, C in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (R, C) in region:
                    perm -= 1
        total += area * perm
        sides = countSides(region, garden)
        print(sides)
        discountTotal += area * sides
    
    print(f"Normal total: {total}")
    print(f"Discounted total: {discountTotal}")