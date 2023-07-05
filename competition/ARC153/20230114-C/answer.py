
n = int(input())
A = list(map(int, input().split()))
print(n)
print(A)

index_plus = []
index_minus = []


for i, a_v in enumerate(A):
    if a_v == 1:
        index_plus.append(i)
    else:
        index_minus.append(i)

print(n//2)
print(index_plus, index_minus)