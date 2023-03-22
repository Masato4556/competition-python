from collections import defaultdict

n, m = map(int, input().split())
S = []
for _ in range(n):
    S.append(input())

# TODO キャッシュ
def f(s):
    if s in S:
        return S.index(s)
    
    return -
    
# TODO おける_の数を考える

T = defaultdict(set)
for _ in range(n):
    t = input()

    i = 0
    flg = 1
    h = []
    h2 = []
    for j in range(len(t)):
        if flg == 1 and t[j] == "_":
            print(t[i:j])
            a = f(t[i:j])
            if a == -1: break
            h.append(a)
            i = j
            flg *= -1
        
        if flg == -1 and t[j] != "_":
            h2.append(j-i)
            print(t[i:j])
            i = j
            flg *= -1
            
        j += 1

    a = f(t[i:])
    if a != -1: 
        h.append(a)

    if len(h) != n: break
    print(h, h2)
            


    T[tuple(h)].add(tuple(h2))


print(T)
