def tie_knot(lengths, r=256):
    circle = [x for x in range(0, r)]
    currpos = 0
    skip = 0
    for length in lengths:
        start = currpos
        end = (currpos + length) % len(circle)
        # print("--------------")
        # print("Circle", circle)
        # print("Current Position:", currpos, "Skip size:", skip)
        # print("Start:", start, "End:", end)
        circle_hist = circle[:]
        if end > start:
            circle[start:end] = [x for x in reversed(circle[start:end])]
        elif end == start:
            rev = [x for x in reversed(circle[start:] + circle[:end])]
            circle[start:] = rev[:-end]
            circle[:end] = rev[-end:]
        else:
            rev = [x for x in reversed(circle[start:] + circle[:end])]
            circle[start:] = rev[:-end]
            print(len(circle))
            circle[:end] = rev[-end:]
            print(len(circle))
        
        if len(circle) != len(circle_hist):
            print("Error! circle has been degraded.")
            print("Old Circle:", circle_hist, "Length: ", len(circle_hist))
            print("New Circle:", circle, "Length: ", len(circle))
            print("Start:", start, "End:", end)
            print("Rev:", rev)
            return None
        
        currpos = (currpos + length + skip) % len(circle)
        skip += 1
        
        
            
            
        
    return circle[0]*circle[1]