import math, sys

def calc_steps(input_value):
    # Consider the smallest square spiral in which the input value would be located
    order = math.ceil(math.sqrt(input_value))
    # Determine the location of 1 from the order of the square
    oneloc = int(order/2)
    
    # The range of values including the input value that are added to the 
    # spiral to transition from a square of order n to n + 1.
    range_to_add = range((order - 1)**2 + 1, (order)**2 + 1)
    
    # Determine the positional offset of the first range value wrt the location
    # of 1.
    coeff = -1 if order % 2 == 0 else 1
    first_offset = int(order/2)*coeff
    if coeff == -1: first_offset += 1
    
    offset = first_offset
    offsets = []
    iresult = -1
    
    for i, n in enumerate(range_to_add):
        offsets.append(offset)
        if i < int(len(range_to_add)/2): offset -= coeff
        if n == input_value: iresult = i
    
    resultrow = offsets[iresult] + oneloc
    resultcol = offsets[len(offsets) - 1 - iresult] + oneloc
    
    return int(math.fabs(resultrow - oneloc) + math.fabs(resultcol - oneloc))


