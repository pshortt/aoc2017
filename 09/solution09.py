class StreamProc():
    def __init__(self, line):
        openers = []
        self.ngroups = 0
        ignore_next = False
        score = 0
        self.totscore = 0
        self.ngarbage = 0
        for c in line:
            if not ignore_next:
                if peek(openers) != '<':    
                    if c == '{':
                        openers.append(c)
                        score += 1
                        self.totscore += score
                    elif c == '<':
                        openers.append(c)
                    elif c == '}':
                        openers.pop()
                        self.ngroups += 1   
                        score -= 1
                elif c == '!':
                    ignore_next = True
                elif c == '>':
                    openers.pop()
                else:
                    self.ngarbage += 1
            else:
                ignore_next = False


def peek(s):
    if len(s) == 0: return None
    else: return s[len(s) - 1]