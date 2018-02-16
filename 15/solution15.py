def genseq(seed, factor, length=4*10**7, fmult=1, mod=2147483647):
    seq = []
    seq.append(seed*factor % mod)
    while len(seq) < length:
        n = seq[-1:][0]*factor % mod
        if n % fmult == 0:
            seq.append(n)
    return seq
    
def judge(a, b, f=16):
    return binfill(a, f)[-f:] == binfill(b, f)[-f:]
    
def binfill(x, f):
    return bin(x)[2:].zfill(f)
    
def count_judge(seedA, seedB, length=4*10**7, fmultA=1, fmultB=1, factA=16807, factB=48271):
    seqA = genseq(seedA, factA, length, fmultA)
    seqB = genseq(seedB, factB, length, fmultB)
    to_judge = [(seqA[i], seqB[i]) for i in range(len(seqA))]
    judged = map(lambda t: judge(*t), to_judge)
    return sum(judged)