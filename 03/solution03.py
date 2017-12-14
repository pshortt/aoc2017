import math, sys

def calc_steps(input_value):
    order = math.ceil(math.sqrt(input_value))
    oneloc = int(order/2)
    
    coeff = -1 if order % 2 == 0 else 1
    first_offset = int(order/2)*coeff
    first_offset += 1 if coeff == -1 else ;
    
    offset = first_offset
    offsets = []
    iresult = -1
    range_to_add = range((order - 1)**2 + 1, (order)**2 + 1)
    
    for i, n in enumerate(range_to_add):
        offsets.append(offset)
        if i < int(len(range_to_add)/2): offset -= coeff
        if n == input_value: iresult = i
    
    resultrow = offsets[iresult] + oneloc
    resultcol = offsets[len(offsets) - 1 - iresult] + oneloc
    
    return int(math.fabs(resultrow - oneloc) + math.fabs(resultcol - oneloc))


