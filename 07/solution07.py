import re

class Program():
    def __init__(self, line):
        self.children_names = []
        self.children = []
        ne = re.search(r'(^[a-z]*)\s', line)
        self.name = ne.group(1)
        we = re.search(r'\(([0-9]*)\)', line)
        self.weight = int(we.group(1))
        ce = re.search(r'>\s([a-z,\s]*)', line)
        if ce is not None:
            self.children_names.extend([p.strip() for p in ce.group(1).split(',')])
    
    def add_child(self, p):
        self.children.append(p)
    
    def total_weight(self):
        weight = self.weight
        for p in self.children:
            weight += p.total_weight()
        return weight
    
    def balance_report(self):
        unique_weights = []
        corr_programs = []
        for p in self.children:
            tw = p.total_weight()
            if tw in unique_weights:
                corr_programs[unique_weights.index(tw)].append(p.name)
            else:
                unique_weights.append(tw)
                corr_programs.append([p.name])
        
        return {'uw':unique_weights, 'cp':corr_programs}
    
    def __str__(self):
        return '{} ({}) -> {}'.format(self.name,
                                      self.weight,
                                      self.children)

class Tower():
    def __init__(self, fname):
        f = open(fname)
        self.programs = []
        found_children = []
        
        for l in f:
            p = Program(l)
            found_children.extend(p.children_names)
            self.programs.append(p)
        f.close()  
        
        roots = []
        for p in self.programs:
            if p.name not in found_children:
                roots.append(p)
            for c in p.children_names:
                p.add_child(self.get_program(c))
                
        if len(roots) > 1:
            print("Error: found more than one root: {}".format(roots))
        self.root = roots[0]
        
        
    def get_program(self, pname):
        for p in self.programs:
            if p.name == pname: return p
        return None
    
    def balance_tower(self):
        new_weight = -1
        delta = 0
        p = self.root
        while new_weight < 0:
            br = p.balance_report()
            if len(br['uw']) == 2:
                if len(br['cp'][0]) == 1:
                    delta = br['uw'][1] - br['uw'][0]
                    p = self.get_program(br['cp'][0][0])
                else:
                    delta = br['uw'][0] - br['uw'][1]
                    p = self.get_program(br['cp'][1][0])
            elif len(br['uw']) == 1:
                new_weight = p.weight + delta
        return new_weight
    
    def __str__(self):
        return 'root: {} programs: {}'.format(self.root, self.programs)

if __name__ == '__main__':
    t = Tower('example_input.txt')
    print(t.balance_tower())
    
