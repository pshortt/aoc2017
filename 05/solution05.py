def solve_maze_p1(fname):
    return solve_maze(fname, make_incrementor())

def solve_maze_p2(fname):
    return solve_maze(fname, make_gt3_check())

def make_incrementor():
    return lambda x: x + 1
    
def make_gt3_check():
    return lambda x: x + 1 if x < 3 else x - 1
    
def solve_maze(fname, xform):
    maze = parse_maze_file(fname)
    reg = 0
    njumps = 0
    while reg < len(maze):
        tmp = reg
        reg += maze[reg]
        if reg < 0: reg = 0
        maze[tmp] = xform(maze[tmp])
        njumps += 1
        
    return [njumps, maze]
    
def parse_maze_file(fname):
    f = open(fname, 'r')
    maze = [int(line) for line in f]
    f.close()
    return maze