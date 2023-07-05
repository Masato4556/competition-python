
H, W, K = map(int, input().split())

PH = []
for i in range(H):
    PH.append((i + 1) ** K * (H-i))
    for j in range(i):
        PH[i] -= PH[j]

print(H ** K)
print(PH)