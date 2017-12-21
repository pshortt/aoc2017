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
    
    def __str__(self):
        return 'root: {} programs: {}'.format(self.root, self.programs)
