import os, time

class Firewall():
    def __init__(self, fname, delay=0, animate=False, calc_sev=True):
        f = open(fname)
        nlayers = 0
        self.layers = []
        # assume layers numbers are sorted in input file
        for line in f:
            li = [int(s) for s in line.split(': ')]
            layer_number = li[0]
            length = li[1]
            while nlayers < layer_number:
               self.layers.append(0)
               nlayers += 1
            self.layers.append(length)
            nlayers += 1
        f.close()
        
        self.positions = [0 for i in range(0, nlayers)]
        self.directions = [1 for i in range(0, nlayers)]
        self.enemy_pos = -1
        self.severity = 0
        self.delay = delay
        self.animate = animate
        self.caught = False
        self.calc_sev = calc_sev
        # self.run()
        self.run_new()
            
    def __str__(self):
        res = ''
        for i, length in enumerate(self.layers):
            prefix = '{}: '.format(i)
            suffix = ['[ ]' for i in range(0, length)]      
            if not suffix:
                suffix = ['...']
            else:
                suffix[self.positions[i]] = '[S]';
                
            if self.enemy_pos == i:
                s = suffix[0]
                suffix[0] = '(' + s[1:-1] + ')'
                
            suffix = " ".join(suffix).strip()
            res += prefix + suffix + '\n'
        return res
        
    def tick(self):
        for i,p in enumerate(self.positions):
            if self.layers[i] > 0:
                p += self.directions[i]
                self.positions[i] = p
                if p == self.layers[i]-1 or p == 0:
                    self.directions[i] *= -1

    def run(self):
        for i in range(0, self.delay):
            self.tick()
            self.render()
            
        for i in range(0, len(self.layers)):                
            self.enemy_pos += 1
            self.render()
            if self.positions[i] == 0 and self.layers[i] > 0:
                self.caught = True
                # print("CAUGHT")
                if self.calc_sev:
                    self.severity += self.layers[i]*(i)
                else:
                    return None
            self.tick()
            self.render()
    
    def run_new(self):
        for i in range(self.delay, self.delay + len(self.layers)):
            ind = i - self.delay
            # print("Time:", i, "Range:", self.layers[ind], "Check:", i % (self.layers[ind] - 1)*2 and self.layers[ind] > 0)
            if i % ((self.layers[ind] - 1)*2) == 0 and self.layers[ind] > 0:
                self.caught = True
                # print("CAUGHT AT", ind)
                if self.calc_sev:
                    self.severity += self.layers[ind]*ind
                else:
                    return None
                    
    def render(self):
        clear = lambda: os.system('cls')
        if self.animate:
                print(self)
                time.sleep(1)
                clear()

def break_firewall(fname):
    delay = 0
    f = Firewall(fname, delay, False, False)
    
    while f.caught:
        delay += 1
        f = Firewall(fname, delay, False, False)
        
    return delay
    