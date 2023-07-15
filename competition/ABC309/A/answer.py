
A, B = map(int, input().split())

print("Yes" if B-A == 1 and (B-1)//3 == (A-1) // 3 else "No")
