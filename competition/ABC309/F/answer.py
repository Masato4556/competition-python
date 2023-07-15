N = int(input())
cubes = []
W = []
D = []
for i in range(N):
    cube = list(map(int, input().split()))
    cube.sort()
    cubes.append(cube)

cubes.sort()
for cube in cubes:
    W.append([cube[1], i])
    D.append([cube[2], i])


for i in range(N):
    s = set(range(1, N))
    for j in range(N):

        if cubes[i][1] < cubes[j][1] and cubes[i][2] < cubes[j][2]:
            print("Yes")
            exit()

print("No")
