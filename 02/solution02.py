def checksum(fname):
    sum = 0
    f = open(fname)
    lines = [line.split() for line in f]
    f.close()
    for line in lines:
        cells = [int(cell) for cell in line]
        sum += max(cells) - min(cells)
    
    return sum