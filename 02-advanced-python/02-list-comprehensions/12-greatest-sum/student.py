#import math
#
#def greatest_sum(ns):
#    greatest = -math.inf
#    for i in range(0,len(ns)):
#        for j in range(i+1,len(ns)+1):
#            if sum(ns[i:j])>greatest:
#                greatest=sum(ns[i:j])
#                pair = (i,j)
#    return pair

def greatest_sum(ns):
    def slice_sum(pair):
        i, j = pair
        return sum(ns[i:j])
    return max([(i,j) for i in range(0,len(ns)+1) for j in range(i+1, len(ns)+1)], key=slice_sum)