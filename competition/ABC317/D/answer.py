from collections import defaultdict
N = int(input())


def calcNumberexceedY(x, y):
    if x > y:
        return 0

    return (y-x) // 2 + 1


areas = []
base = 0
all_z = 0
for i in range(N):
    x, y, z = map(int, input().split())
    all_z += z
    if x > y:
        base += z
        continue
    areas.append((calcNumberexceedY(x, y), z))  # 現在議席を確保できていない選挙区だけを追加する

required_z = calcNumberexceedY(base, all_z - base)
area_num = len(areas)


dp = [defaultdict(lambda: 10**16) for _ in range(area_num+1)]
dp[0][0] = 0
for i in range(area_num):
    v, z = areas[i]
    for prev_z in dp[i].keys():
        # i番目の選挙区の議席を取得しないケース
        dp[i+1][prev_z] = min(dp[i+1][prev_z], dp[i][prev_z])

        # i番目の選挙区の議席を取得するケース
        next_z = min(prev_z+z, required_z)
        dp[i+1][next_z] = min(dp[i+1][next_z], dp[i][prev_z]+v)
        # 必要最低限以上の議席を確保した場合も、必要最低限の議席を確保したものとして扱うことで
        # dp[-1][required_z]で回答が得られるようになる

print(dp[-1][required_z])
