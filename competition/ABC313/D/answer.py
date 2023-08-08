N, k = map(int, input().split())

A = [-1] * N

answers = []
for i in range(k+1):
    query = [j+1 for j in range(k+1) if j != i]
    print("?", *query)
    answers.append(int(input()))

s = sum(answers) % 2
for i in range(k+1):
    if s == answers[i]:
        A[i] = 0
    else:
        A[i] = 1

base_querey = [i+1 for i in range(k-1)]
base_s = sum([answers[i] for i in range(k-1)]) % 2
for i in range(k+1, N):
    query = base_querey.copy()
    query.append(i+1)
    print("?", *query)
    if int(input()) == base_s:
        A[i] = 0
    else:
        A[i] = 1
print("!", *A)
