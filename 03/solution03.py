import math, sys

def calc_steps(input_value, p2_flag):
    spiral = build_spiral(input_value, p2_flag)
    if p2_flag:
        
        return spiral[len(spiral) - 1][3]
        
    else:
        
        return distance(spiral[0], spiral[input_value - 1])


def build_spiral(input_value, p2_flag):
    order = math.ceil(math.sqrt(input_value))
    if p2_flag and is_square(input_value):
        order += 1
    spiral = [];
    for n in range(1, order + 1):
        range_to_add = range((n - 1)**2 + 1, (n)**2 + 1)
        coeff = -1 if n % 2 == 0 else 1
        first_offset = n // 2*coeff
        if coeff == -1: first_offset += 1
        offset = first_offset
        offsets = [] 
        
        for i, m in enumerate(range_to_add):
            offsets.append(offset)
            if i < int(len(range_to_add)/2):
                offset -= coeff
                
        for i, m in enumerate(range_to_add):
            if p2_flag:
                if len(spiral) == 0:
                    node = (m, offsets[i], offsets[len(offsets) - 1 - i], 1)
                    spiral.append(node)
                else:
                    sum = 0
                    node = (m, offsets[i], offsets[len(offsets) - 1 - i])
                    for t in spiral:
                        if int(math.fabs(t[1] - node[1])) <= 1 and int(math.fabs(t[2] - node[2])) <= 1:
                            sum += t[3]
                    spiral.append((node[0], node[1], node[2], sum))
                    if sum > input_value: return spiral
            else:
                spiral.append((m, offsets[i], offsets[len(offsets) - 1 - i]))
    return spiral

    
def distance(fr, to):
    return int(math.fabs(fr[1] - to[1]) + math.fabs(fr[2] - to[2]))
    
# thanks to https://stackoverflow.com/users/95810/alex-martelli
# https://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True