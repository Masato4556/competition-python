
from itertools import combinations

def f(A, B, delete_rs, delete_cs):
    br = 0
    bc = 0
    for ar in range(ha):
        if ar in delete_rs: continue
        for ac in range(wa):
            if ac in delete_cs: continue
            if A[ar][ac] != B[br][bc]: return False
            bc += 1
        bc = 0
        br += 1
    
    return True

ha, wa = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(ha)]

hb, wb = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(hb)]

if (ha < hb) or (wa < wb): 
    print("No")
    exit()

ans = False
for delete_rs in combinations(range(ha), ha - hb):
    for delete_cs in combinations(range(wa), wa - wb):
        if f(A, B, delete_rs, delete_cs):
            print("Yes")
            exit()

print("No")
        
                

