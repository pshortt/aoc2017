def spinlock(steps, n):
    buffer = [0]
    pos = 0
    for x in range(n):
        pos += steps
        pos %= len(buffer)
        pos += 1
        buffer.insert(pos, x + 1)
    return buffer
    
def short_circuit(steps, n=2017):
     buffer = spinlock(steps, n)
     pos = buffer.index(n)
     return buffer[(pos + 1) % len(buffer)]