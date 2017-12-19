import re

class Program():
    def __init__(self, line):
        self.children = []
        ne = re.search(r'(^[a-z]*)\s', line)
        self.name = ne.group(1)
        we = re.search(r'\(([0-9]*)\)', line)
        self.weight = we.group(1)
        ce = re.search(r'>\s([a-z,\s]*)', line)
        if ce is not None:
            self.children.extend([p.strip() for p in ce.group(1).split(',')])
            
    
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
            found_children.extend(p.children)
            self.programs.append(p)
        f.close()  
        roots = []
        for p in self.programs:
            if p.name not in found_children:
                roots.append(p)
        if len(roots) > 1:
            print("Error: found more than one root: {}".format(roots))
        self.root = roots[0]
        
    def __str__(self):
        return 'root: {} programs: {}'.format(self.root, self.programs)
