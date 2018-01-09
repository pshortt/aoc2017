class Program():
    def __init__(self, inp_str):
        words = inp_str.split()
        self.id = int(words[0])
        self.pipes = [int(p.split(',')[0]) for p in words[2:]]
    
    def get_nodes(self):
        res = [id]
        return res.extend(self.pipes)
    
    def __str__(self):
        return '{} <-> {}'.format(self.id, self.pipes)
        
class Village():
    def __init__(self, inp):
        f = open(inp)
        self.programs = [Program(line) for line in f]
        f.close()
    
    def __str__(self):
        return '{}'.format([str(p) for p in self.programs])
        
    def get_network(self, id):
        found_new = True
        network = []
        current_p = self.get_program(id)
        path = []
        traveled = [current_p.id] 
        while found_new:
            for p in current_p.pipes:   
                if p not in network:
                    network.append(p)
                if p not in traveled:
                    path.append(p)
            traveled.append(current_p.id)
            if len(path) == 0:
                found_new = False
            else:
                current_p = self.get_program(path.pop())
        network.sort()
        return network
    
    def n_groups(self):
        ids = [p.id for p in self.programs]
        found_ids = []
        n_groups = 0
        for id in ids:
            if id not in found_ids:
                found_ids.extend(self.get_network(id))
                n_groups += 1
            
        
        return n_groups
            
    def get_program(self, id):
        for p in self.programs:
            if p.id == id:
                return p
        return None
        