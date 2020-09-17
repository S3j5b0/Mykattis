# Parse 
import sys

class Interval:
    def __init__(self, head, tail, val):
        
        self.head = int(head)
        self.tail = int(tail)
        self.val = int(val) 

    def __repr__(self):
        return  "|  head: " + str(self.head) + " tail: " + str(self.tail) + " value: " + str(self.val) + " |"
def parse():
    indexC = 1
    Allintervals = []
    Allintervals.append(Interval(-100, -100, 0))
    for line in sys.stdin:
        current = line.strip().split()
        if (len(current) == 1):
            n = current
        else:
            currentInter = Interval(current[0], current[1], current[2])
            Allintervals.append(currentInter)
    return Allintervals         



def solver(IntervalSet):
    M = [None] * (len(IntervalSet)) 

    sortedSet = sorted(IntervalSet, key=lambda x: x.tail)


    def iter_compute_opt(J):
        M[0] = 0

        for u in range(1, J+1):
            r = M[pn(u)]
 
            M[u] = max(IntervalSet[u].val + r,M[u-1] )
        print(M[len(M)-1])


    def pn(jEnd1):
        if jEnd1 == 0:
            return 0
        low = 0 
        hi = len(IntervalSet)

        while(low <= hi):
            mid = (low + hi) // 2
            if sortedSet[mid].tail <= sortedSet[jEnd1].head:
                if sortedSet[mid + 1].tail <= sortedSet[jEnd1].head:
                    low = mid + 1
                else:
                    return mid
            else:
                hi = mid -1
        return 0    
    iter_compute_opt(len(sortedSet)-1)






set = parse()

solver(set)


