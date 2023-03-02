pos = []
for _ in range(4):
    pos.append(tuple(map(int, input().split())))

# 対角線
def f0_2(p):
    return (pos[0][0] - pos[2][0]) * (p[1] - pos[2][1]) - (pos[0][1] - pos[2][1]) * (p[0] - pos[2][0])

def f1_3(p):
    return (pos[1][0] - pos[3][0]) * (p[1] - pos[3][1]) - (pos[1][1] - pos[3][1]) * (p[0] - pos[3][0])

# ２つの対角線において、対角線がその対角線に用いられていない残り2点の間を通る = 四角形が凸
if f0_2(pos[1]) * f0_2(pos[3]) < 0 and f1_3(pos[0]) * f1_3(pos[2]) < 0:
    print("Yes")
else:
    print("No")
