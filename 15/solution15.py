def gen(seed, factor, fmult, mod=2147483647):
    x = seed
    while True:
        x *= factor
        x %= mod
        if x % fmult == 0:
            yield x
    
def count_matches(length, seedA, seedB, fmultA=1, fmultB=1):
    genA = gen(seedA, 16807, fmultA)
    genB = gen(seedB, 48271, fmultB)
    
    ctr = 0
    
    for x in range(length):
        if (next(genA) & 0xFFFF) == (next(genB) & 0xFFFF):
            ctr += 1
            
    return ctr