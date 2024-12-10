import sys
sys.setrecursionlimit(10000)

def printFilemap(filemap):
    line = ""
    for id, length in filemap:
        if id == -1:
            line += "." * length
        else:
            line += str(id) * length
    print(line)

def fillFiles(filemap):
    for fileID, length in [f for f in filemap[::-1] if f[0] != -1]:
        for i in range(filemap.index((fileID, length))):
            s = filemap[i]
            if s[0] == -1 and i < filemap.index((fileID, length)) and s[1] >= length:
                # printFilemap(filemap)
                if s[1] > length:
                    filemap[i] = (s[0], s[1] - length)
                    filemap[filemap.index((fileID, length))] = (-1, length)
                    filemap.insert(i, (fileID, length))
                    break
                elif s[1] == length:
                    filemap[filemap.index((fileID, length))] = (-1, length)
                    filemap[i] = (fileID, length)
                    break
    # printFilemap(filemap)
    return filemap
                        

with open("day9input.txt", "r") as input:
    filemap = []

    file = True
    fileID = 0
    for digit in input.readlines()[0]:
        if file:
            filemap.append((fileID, int(digit)))
            fileID += 1
        else:
            filemap.append((-1, int(digit)))
        file = not file

    checksum = 0

    filled = fillFiles(filemap)

    i = 0
    for fileID, length in filled:
        if fileID != -1:
            for n in range(i, i + length):
                checksum += fileID * n
        i += length

    print(checksum)
