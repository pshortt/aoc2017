def proc_dancefile(dancefile):
    f = open(dancefile)
    content = f.read()
    f.close()
    return content.split(',')

def spin(programs, arg):
    pos = int(arg)
    for x in range(pos):
        programs.insert(0, programs.pop())
    return programs

def exchange(programs, arg):
    args = [int(s) for s in arg.split('/')]
    tmp = programs[:]
    programs[args[0]] = tmp[args[1]]
    programs[args[1]] = tmp[args[0]]
    return programs
    
def partner(programs, arg):
    args = arg.split('/')
    new_arg = str(programs.index(args[0])) + '/' + str(programs.index(args[1])) 
    return exchange(programs, new_arg)
        
def run_dance_move(move, programs):
    type = move[0]
    arg = move[1:]
    if type == 's':
        programs = spin(programs, arg)
    elif type == 'x':
        programs = exchange(programs, arg)
    elif type == 'p':
        programs = partner(programs, arg)
    else:
        print('ERROR: ', type)

def run_dance(dancefile, length=16):
    programs = [chr(x) for x in range(97, 97+length)]
    dance_moves = proc_dancefile(dancefile)
    for move in dance_moves:
        run_dance_move(move, programs)
    return ''.join(programs)
    
