

N = int(input())
cards = []


cnt = 0

ans = 0
min_diff = float('inf')
for i in range(N):
    a, b = map(int, input().split())
    cards.append((a, b))
    ans += max(a, b)
    if a - b > 0:
        cnt += 1
    min_diff = min(min_diff, abs(a-b))

print(ans if cnt % 2 == 0 else ans - min_diff)