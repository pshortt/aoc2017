class KnotHash():
    def __init__(self, input, is_part2, r=256):
        # TODO: implement
        if isinstance(input, str):
            self.lengths = [ord(c) for c in input]
        else:
            self.lengths = input
        
        self.currpos = 0
        self.skip = 0   
        self.sparse = [x for x in range(0, r)]
        if is_part2:
            self.lengths.extend([17, 31, 73, 47, 23])
            for i in range(0, 64):
                self.tie_knot()
        else:  
            self.tie_knot(r)
        
        self.reduce()
        
    def __str__(self):
        # TODO: implement
        return ''.join(["{0:0{1}x}".format(x,2) for x in self.dense])
    
    def tie_knot(self, r=256):
        for length in self.lengths:
            start = self.currpos
            end = ((self.currpos + length) % len(self.sparse))

            if end > start:
                rev = [x for x in reversed(self.sparse[start:end])]
                self.sparse[start:end] = rev
            elif end != start:
                rev = [x for x in reversed(self.sparse[start:] + self.sparse[:end])]
                pvt = len(rev) - end
                self.sparse[start:] = rev[:pvt]
                self.sparse[:end] = rev[pvt:]
            
            self.currpos = (self.currpos + length + self.skip)  % len(self.sparse)
            self.skip += 1
    
    def reduce(self, interval=16):
        reg = 0
        self.dense = []
        for i in range(0, len(self.sparse) // interval):
            slice = self.sparse[reg:reg+interval]
            # print("Reg: ", reg, "Reg + interval: ", reg+interval)
            d_ele = slice[0]
            for s_ele in slice[1:]:
                d_ele ^= s_ele
            self.dense.append(d_ele)
            reg += interval
    