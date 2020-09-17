# Parse 
import sys
from datetime import datetime

sys.setrecursionlimit(10**6) 
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
            M[u] = max(IntervalSet[u].val + M[p(u)],M[u-1] )
        print(M[len(M)-1])


    def compute_opt(j):
        if M[j] != None:
            return M[j]

        elif j == 0: return 0
        else:
            M[j] = max(IntervalSet[j].val + compute_opt((p(j))), compute_opt(j-1))
            return M[j]

    
    def p(jEnd):
        if jEnd == 0:
            return 0
        for i in range(jEnd-1,-1, -1):

            if sortedSet[i].tail <= sortedSet[jEnd].head:
                return i 
    iter_compute_opt(len(sortedSet)-1)


 #   p(sortedSet)



dataset = parse()


solver(dataset)




