def get_alphabet(i):
    return chr(ord('A') + i - 1)

H, W = map(int, input().split())
for _ in range(H):
    for v in map(lambda x: "." if x == "0" else get_alphabet(int(x)), input().split()):
        print(v, end="")
    print()

