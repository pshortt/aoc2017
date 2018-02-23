from collections import deque

def spinlock(steps, n):
    buffer = deque([0])
    for x in range(n):
        buffer.rotate(-steps)
        buffer.append(x + 1)
    return buffer
    
def short_circuit(steps, n=2017):
     buffer = spinlock(steps, n)
     # print(buffer)
     return buffer[0]
     
def after_zero(steps, n=50000000):
    result = -1
    pos = 0
    for x in range(n):
        pos += steps
        pos %= x + 1
        pos += 1
        if pos == 1:
            result = x + 1
    return result
            