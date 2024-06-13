# テストデータ生成など、回答とは関係のないコードを実行するファイル
from itertools import combinations
from pprint import pprint


def generate_all_case(n):
    cases = []
    for i in range(1, 2**n):
        case = set()
        for j in range(n):
            if (i >> j) & 1:
                case.add(j)
        cases.append(case)

    return cases


N = 100

all_case = [generate_all_case(i) for i in range(0, N+1)]

dp = [[[] for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for k in range(1, N+1):
        for case in all_case[i]:
            if len(case) == 1:
                dp[i][k].append(case)
                continue

            is_valid = True
            for a, b in combinations(case, 2):
                if abs(a-b) < k:
                    is_valid = False
                    break
            if is_valid:
                dp[i][k].append(case)

for i in range(1, N+1):
    for k in range(1, i+1):
        print(i, k, ':', len(dp[i][k]))
