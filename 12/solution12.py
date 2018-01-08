class Program():
    def __init__(self, inp_str):
        words = inp_str.split()
        self.id = int(words[0])
        self.pipes = [int(p.split(',')[0]) for p in words[2:]]
        
    def __str__(self):
        return '{} <-> {}'.format(self.id, self.pipes)
        
class Village():
    def __init__(self, inp):
        f = open(inp)
        self.programs = [Program(line) for line in f]
        f.close()
    
    def __str__(self):
        return '{}'.format([str(p) for p in self.programs])