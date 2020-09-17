import sys
intervals = []

def P(a,j: int) -> int:
    print("a", a)
    print("j " , j)
    lo = 0
    hi = len(a)

    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid][1] <= a[j][0]:
            if a[mid + 1][1] <= a[j][0]:
                lo = mid + 1 
            else:
                return mid 
        else:
            hi = mid -1 
    return -1

def OPT(a):
    M = [0] * (N+1) 
    for j in range(N):
        if j == -1:
            res = 0
        elif j == 0:
            res = a[0][2]
        else:
            drop = M[j-1]
            take = a[j][2] + M[P(a,j)]
            res = max(drop, take)
        M[j] = res
    print(M[-2])
    return M[-2]

N = int(input())

for i in range(N):
    s , f ,w = input().split(" ")
    intervals.append((int(s), int(f), int(w)))

intervals.sort(key= lambda x: x[1])

print(OPT(intervals))






