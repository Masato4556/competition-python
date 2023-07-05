n = int(input())
s = input()

pos = (0,0)
seen = set()
seen.add((0,0))

move = {
    "U": (0,1),
    "D": (0,-1),
    "R": (1,0),
    "L": (-1,0)
}

for i in range(len(s)):
    pos = (pos[0] + move[s[i]][0], pos[1] + move[s[i]][1])
    if pos in seen:
        print("Yes")
        exit()
    seen.add(pos)

print("No")