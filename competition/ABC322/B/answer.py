N, M = map(int, input().split())
S = input()
T = input()

isPrefix = S == T[0:len(S)]
isSuffix = S == T[-len(S): len(T)]

if isPrefix and isSuffix:
    print(0)
elif isPrefix:
    print(1)
elif isSuffix:
    print(2)
else:
    print(3)
