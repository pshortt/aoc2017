class RedistInfLoopCheck():
    def __init__(self, banks):
        banks_hist = [banks]
        found_repeat = False
        self.ctr = 0
        while not found_repeat:
            banks = iterate_banks(banks[:])
            found_repeat = banks in banks_hist
            self.ctr += 1
            banks_hist.append(banks)
    
        self.ncycles = len(banks_hist[banks_hist.index(banks):]) - 1
    
def iterate_banks(banks):
    reg = banks.index(max(banks))
    to_redist = banks[reg]
    banks[reg] = 0
    while to_redist > 0:
        reg += 1
        to_redist -= 1
        banks[reg % len(banks)] += 1
    return banks