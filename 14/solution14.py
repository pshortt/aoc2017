from s10.solution10 import KnotHash

def count_blocks(inp):
    sum = 0
    disk = generate_disk(inp)
    for row in disk:
        sum += row.count('1')
    return sum
    
def generate_disk(inp):
    disk = [];
    for i in range(128):
        locinp = inp + '-' + str(i)
        hash = str(KnotHash(locinp))
        disk.append(generate_row(hash))
    return disk
        
def generate_row(hash):
    split_hash = [hb for hb in hash]
    
    return list(''.join([bin(int(hb, 16))[2:].zfill(4) for hb in split_hash]))
    
def neighbours(pos, length=128):
    neighs = [(-1, 0), (1, 0), (0, -1) , (0, 1)]
    
    f = lambda t: tuple([x + pos[i] for i, x in enumerate(t)])
    neighs = map(f, neighs)
    neighs = [n for n in neighs] 
    
    c = lambda t: all([x in range(0,length) for x in t])  
    neighs = filter(c, neighs)
    return [n for n in neighs]
    
                
 def next_node():               
