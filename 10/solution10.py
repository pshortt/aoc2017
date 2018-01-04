def tie_knot(lengths, r=256):
    circle = [x for x in range(0, r)]
    currpos = 0
    skip = 0
    for length in lengths:
        start = currpos
        end = ((currpos + length) % len(circle))

        if end > start:
            rev = [x for x in reversed(circle[start:end])]
            circle[start:end] = rev
        elif end != start:
            rev = [x for x in reversed(circle[start:] + circle[:end])]
            pvt = len(rev) - end
            circle[start:] = rev[:pvt]
            circle[:end] = rev[pvt:]
        
        currpos = (currpos + length + skip)  % len(circle)
        skip += 1
       
    return circle[0]*circle[1]