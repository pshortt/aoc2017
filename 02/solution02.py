import itertools

def checksum(fname):
    sum = 0
    rows = parsess(fname)
    for row in rows:
        sum += max(row) - min(row)
    
    return sum

def checksum2(fname):
    sum = 0
    rows = parsess(fname)
    for row in rows:
        for comb in itertools.combinations(row, 2):
            if max(comb) % min(comb) == 0:
                sum += max(comb) // min(comb)
       
    return sum

def parsess(fname):
    f = open(fname)
    rows = [row.split() for row in f]
    rows = [[int(cell) for cell in row] for row in rows]
    f.close()
    return rows