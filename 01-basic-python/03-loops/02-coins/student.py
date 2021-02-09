def coins(c1, c2, c5, goal):
    count = 0
    for x in range(0, c1+1):
        for y in range(0, c2+1):
            for z in range(0, c5+1):
                if (z * 5 + y * 2 + x) == goal:
                    return True
    return False