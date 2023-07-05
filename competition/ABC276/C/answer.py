import itertools

def isSorted(l):
    for i in range(len(l)-1):
        if l[i] - l[i+1] > 0:
            return False
    return True

n = int(input())
P = list(map(int, input().split()))

for left in range(len(P)):
    if isSorted(P[left:]):

        v = max([p for p in P[left:] if p < P[left-1]])
        id = P.index(v)

        P[left-1], P[id] = P[id], P[left-1]
        P_temp = P[left:]
        P_temp.sort(reverse= True)
        P = P[:left] + P_temp
        break

print(*P)

