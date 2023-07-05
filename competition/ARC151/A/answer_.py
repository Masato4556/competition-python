N = int(input())
S = int(input(), 2)
T = int(input(), 2)

def count_ones(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>= 1
    return count
res = []
for i in range(2*N):
    if count_ones(i ^ S) != count_ones(i ^ T): continue
    print(("{:0" + str(N) +"b}").format(i))
    exit()

print(-1)