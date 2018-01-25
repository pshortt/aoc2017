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

def next_node(disk, grouped_nodes):
    for i in range(len(disk)):
        for j in range(len(disk)):
            if (i, j) not in grouped_nodes and disk[i][j] != '0':
                return (i, j)
    return None
    
def count_groups(inp):
    disk = generate_disk(inp)
    ngroups = 0
    grouped_nodes = []
    neighs = []
    node = next_node(disk, grouped_nodes)
    f = lambda t: disk[t[0]][t[1]] == '1' and t not in grouped_nodes
    while node is not None:
        grouped_nodes.append(node)
        ngroups += 1
        neighs = [n for n in filter(f, neighbours(node))]
        while len(neighs) > 0:
            neighbour = neighs.pop()
            grouped_nodes.append(neighbour)
            neighs.extend([n for n in filter(f, neighbours(neighbour))])
        node = next_node(disk, grouped_nodes)
        print(ngroups)
    return ngroups
            