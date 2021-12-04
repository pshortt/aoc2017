def solve_part1(filename):
    program = readlines(filename)
    program_counter = 0
    register = {}
    last_frequency_played = None

    while  program_counter < len(program):
        line = program[program_counter]

        instruction = line.split()[0]
        address = line.split()[1]
        if address not in register.keys(): register[address] = 0

        val = line.split()[2] if len(line.split()) > 2 else ''
        if val.isdigit() or val.startswith('-'):
            val = int(val)
        elif val:
            val = register[val]

        incr = 1
        
        match instruction:
            case 'snd':
                last_frequency_played = register[address]
            case 'set':
                register[address] = val
            case 'add':
                register[address] += val
            case 'mul':
                register[address] *= val
            case 'mod':
                register[address] %= val
            case 'rcv':
                if register[address] != 0: return last_frequency_played
            case 'jgz':
                if register[address] > 0: incr = val

        program_counter += incr

def solve_part2(filename):
    return 0

def readlines(filename):
    f = open(filename)
    lines = [l.strip() for l in f.readlines()]
    f.close()

    return lines

if __name__ == '__main__':
    solve_part1('day18/example.input')