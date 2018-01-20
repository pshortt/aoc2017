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
    bin_split = [bin(int(hb, 16))[2:].zfill(4) for hb in split_hash]
    
    return ''.join(bin_split)
                

