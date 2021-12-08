
def solve_part1(filename):
    program = readlines(filename)

    return DuetInterpreter(program, 1).run()

def solve_part2(filename):
    program = readlines(filename)
    duet_interpreter = DuetInterpreter(program, 2)
    result = duet_interpreter.run()
    return result

def readlines(filename):
    f = open(filename)
    lines = [l.strip() for l in f.readlines()]
    f.close()

    return lines

class DuetInterpreter():
    def __init__(self, program, part) -> None:
        self.program = program
        self.part = part
        self.processes = [DuetProcess(x) for x in range(self.part)]
        self.broadcast_queue = ([],[])
         
    def run(self):
        while not all([process.stop_condition for process in self.processes]) and not all([process.waiting for process in self.processes]) :
            for process in self.processes:
                process.stop_condition = process.program_counter >= len(self.program) or process.stop_condition
                if not process.stop_condition:
                    duet_program_line = DuetProgramLine(self.program[process.program_counter])
                    self.check_register(process, duet_program_line)
                    process.run_line(duet_program_line, self.part)
                    if process.broadcasting:
                        self.broadcast_queue_put(process)
                    
        if self.part == 1:
            result = sum([process.last_frequency_played for process in self.processes])
        else:
            result = sum([i*process.send_count for (i,process) in enumerate(self.processes)])

        return result

    def check_register(self, process, duet_program_line):
        if duet_program_line.address.isdigit() or duet_program_line.address.startswith('-'):
            process.register[duet_program_line.address] = int(duet_program_line.address)

        if duet_program_line.address and duet_program_line.address not in process.keys(): 
            process.register[duet_program_line.address] = 0
        
        if duet_program_line.instruction == 'rcv':
            duet_program_line.val = self.broadcast_queue_get(process)
        elif duet_program_line.instruction == 'snd' and duet_program_line.val == '':
            duet_program_line.val = process.get(duet_program_line.address)
        elif duet_program_line.val.isdigit() or duet_program_line.val.startswith('-'):
            duet_program_line.val = int(duet_program_line.val)
        elif duet_program_line.val:
            duet_program_line.val = process.get(duet_program_line.val)
        

    def broadcast_queue_put(self, process):
        self.broadcast_queue[(process.id + 1) % 2].append(process.listen())
    
    def broadcast_queue_get(self, process):
        if len(self.broadcast_queue[process.id]):
            result = self.broadcast_queue[process.id].pop(0)
        else:
            result = ''
        
        return result

class DuetProcess():
    def __init__(self, id) -> None:
        self.register = {'p': id}
        self.id = id
        self.program_counter = 0
        self.incr = 1
        self.last_frequency_played = -1
        self.stop_condition = False
        self.broadcasting = False
        self.waiting = False
        self.send_count = 0
        
    def run_line(self, duet_program_line, part):
        if self.waiting:
            self.rcv2(duet_program_line)
        else:
            match duet_program_line.instruction:
                case 'set':
                    self.set(duet_program_line)
                case 'add':
                    self.add(duet_program_line)
                case 'mul':
                    self.mul(duet_program_line)
                case 'mod':
                    self.mod(duet_program_line)
                case 'snd':
                    if part == 1: 
                        self.snd1(duet_program_line) 
                    else:
                        self.snd2(duet_program_line)
                case 'jgz':
                    self.jgz(duet_program_line)
                case 'rcv':
                    if part == 1: 
                        self.rcv1(duet_program_line) 
                    else:
                         self.rcv2(duet_program_line)       
        self.proceed()

    def keys(self):
        return self.register.keys()

    def get(self, address):
        return self.register[address]

    def set(self, duet_program_line):
        self.register[duet_program_line.address] = duet_program_line.val

    def add(self, duet_program_line):
        self.register[duet_program_line.address] += duet_program_line.val

    def mul(self, duet_program_line):
        self.register[duet_program_line.address] *= duet_program_line.val
    
    def mod(self, duet_program_line):
        self.register[duet_program_line.address] %= duet_program_line.val

    def snd1(self, duet_program_line):
        self.last_frequency_played = self.register[duet_program_line.address]
        self.broadcasting = True

    def snd2(self, duet_program_line):
        self.broadcasting = True
        self.last_frequency_played = duet_program_line.val
        self.send_count += 1

    def jgz(self, duet_program_line):
        if self.get(duet_program_line.address) > 0: self.incr = duet_program_line.val

    def rcv1(self, duet_program_line):
        if self.get(duet_program_line.address) != 0:
            self.stop_condition = True

    def rcv2(self, duet_program_line):
        if duet_program_line.val == '':
            self.waiting = True
        else:
            self.waiting = False
            self.set(duet_program_line)

    def proceed(self):
        if not self.waiting: self.program_counter += self.incr
        self.reset_incr()
    
    def reset_incr(self):
        self.incr = 1

    def listen(self):
        self.broadcasting = False
        return self.last_frequency_played

class DuetProgramLine():
    def __init__(self, text_line) -> None:
        self.instruction = text_line.split()[0]
        self.address = text_line.split()[1]
        self.val = text_line.split()[2] if len(text_line.split()) > 2 else ''

        if self.instruction == 'snd' and self.address.isdigit():
            self.val = self.address
            self.address = ''

if __name__ == '__main__':
    solve_part1('day18/example.input')