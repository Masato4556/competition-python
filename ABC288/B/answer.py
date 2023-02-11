n, k = map(int, input().split())
names = [input() for _ in range(k)]
names.sort()
print("\n".join(names))
