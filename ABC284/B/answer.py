
t = int(input())
for i in range(t):
    input()
    print(sum([i % 2 == 1 for i in map(int, input().split())]))
