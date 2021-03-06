import re, collections

class Instruction():
    def __init__(self, l):
        exp = r'([a-z]*)\s((?:in|de)c)\s([-0-9]*)\sif\s([a-z]*)\s([><=!]{1,2})\s([-0-9]*)'
        sr = re.search(exp, l)
        self.reg = sr.group(1)
        self.op = sr.group(2)
        self.arg = int(sr.group(3))
        self.condreg = sr.group(4)
        self.condop = sr.group(5)
        self.condarg = int(sr.group(6))
        
    def __str__(self):
        return '{} {} {} if {} {} {}'.format(self.reg, self.op, self.arg,
                                          self.condreg, self.condop, 
                                          self.condarg)
    
    def eval_cond(self, memval):
        fx = self.parse_bool_cond()
        return fx(memval, self.condarg)
    
    def get_op(self):
        if self.op == 'inc':
            return lambda x, y: x + y
        elif self.op == 'dec':
            return lambda x, y: x - y
        else:
            print('Erroneous memeory operation')
            return None
    
    def parse_bool_cond(self):
        if self.condop == '==':
            return lambda x, y: x == y
        elif self.condop == '!=':
            return lambda x, y: x != y
        elif self.condop == '>':
            return lambda x, y: x > y
        elif self.condop == '<':
            return lambda x, y: x < y
        elif self.condop == '>=':
            return lambda x, y: x >= y
        elif self.condop == '<=':
            return lambda x, y: x <= y
        else:
            print('Erroneous condition operator')
            return None
 
class InstructionSet():
    def __init__(self, fname):
        self.instructions = []
        f = open(fname)
        for l in f:
            self.instructions.append(Instruction(l))
        f.close()
         
        self.memory = dict()
        for ins in self.instructions:
            if not isinstance(self.memory.keys, collections.Iterable) or ins.reg not in iter(self.memory):
                self.memory[ins.reg] = 0
        self.execute()
    
    def execute(self):
        self.record = []
        for ins in self.instructions:
            if ins.eval_cond(self.memory[ins.condreg]):
                newval = ins.get_op()(self.memory[ins.reg], ins.arg)
                self.record.append(newval)
                self.memory[ins.reg] = newval
    
    def largest_value(self):
        return max(self.memory.values())
    
    def largest_hist_value(self):
        return max(self.record)
if __name__ == '__main__':
    insset = InstructionSet('example_input.txt')
    print(insset.memory)