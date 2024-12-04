import re

with open("day3/input.txt", "r") as inputLines:
    input = "".join(inputLines)

    print(sum(int(mul.split(",")[0][4::]) * int(mul.split(",")[1][:-1:]) for mul in re.findall(r"mul\([0-9]+,[0-9]+\)", input)))

    print("\n\n".join([input.split("don't()")[0]] + re.findall(r"do\(\).+don't\(\)|do\(\).+", input)))
    print(sum(sum(int(mul.split(",")[0][4::]) * int(mul.split(",")[1][:-1:]) for mul in re.findall(r"mul\([0-9]+,[0-9]+\)", doable)) for doable in [input.split("don't()")[0]] + re.findall(r"do\(\).+don't\(\)|do\(\).+", input)))
    