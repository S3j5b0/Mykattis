# Parse 
import sys
class Interval:
    def __init__(self, head, tail, val):
        self.head = int(head)
        self.tail = int(tail)
        self.val = int(val) 

    def __repr__(self):
        return " | head: " + str(self.head) + " tail: " + str(self.tail) + " value: " + str(self.val) + " |"

Allintervals = []
for line in sys.stdin:
    current = line.strip().split()
    if (len(current) == 1):
        n = current
    else:
        currentInter = Interval(current[0], current[1], current[2])
        Allintervals.append(currentInter)


for i in Allintervals:
    print(i)




