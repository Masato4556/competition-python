n = int(input())
A = list(map(int, input().split()))
Ao = [a for a in A if a % 2 == 1]
Ae = [a for a in A if a % 2 == 0]

Ao.sort()
Ae.sort()

ro = Ao[-1] + Ao[-2] if len(Ao) >= 2 else -1
re = Ae[-1] + Ae[-2] if len(Ae) >= 2 else -1
print(max(ro, re))