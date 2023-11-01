N = int(input())

while True:
    a, b, c = [int(v) for v in str(N)]
    
    if a*b == c:
        print(N)
        break
    N += 1