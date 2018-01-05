import math

class HexGridDist():
    def __init__(self, path):
        self.travel(path)
        self.min_steps = self.calc_min_steps()
        self.max_hist_dist = max(self.dist_hist)
        
    def travel(self, s):
        moves = s.split(',')
        self.pos = (0, 0, 0)
        self.dist_hist = []
        for move in moves:
            self.execute_move(move)
            self.dist_hist.append(self.calc_min_steps())
        
    def execute_move(self, move):
        if move == 'nw':
            self.pos = (self.pos[0] - 1, self.pos[1] + 1, self.pos[2])
        elif move == 'n':
            self.pos = (self.pos[0], self.pos[1] + 1, self.pos[2] - 1)
        elif move == 'ne':
            self.pos = (self.pos[0] + 1, self.pos[1], self.pos[2] - 1)
        elif move == 'se':
            self.pos = (self.pos[0] + 1, self.pos[1] - 1, self.pos[2])
        elif move == 's':
            self.pos = (self.pos[0], self.pos[1] - 1, self.pos[2] + 1)
        elif move == 'sw':
            self.pos = (self.pos[0] - 1, self.pos[1], self.pos[2] + 1)
       
    def calc_min_steps(self):
        return int(math.fabs(self.pos[0]) + math.fabs(self.pos[1]) + math.fabs(self.pos[2])) // 2