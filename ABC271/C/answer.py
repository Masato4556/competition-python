n = int(input())
A = []
A_set = set()

sell_a = 10 ** 10

for a in map(int, input().split()):
    if a in A_set: 
        A.append(sell_a)
    else:
        A.append(a)
    A_set.add(a)

A.sort()
    
result = 0
r_i = n
i = 0 
while i < r_i :
    if A[i] == result+1: 
        i += 1
        result += 1
        continue
    
    if r_i - i < 2: 
        break
        
    r_i -= 2
    A[r_i] = A[r_i +1] = 0
    result += 1

print(result)