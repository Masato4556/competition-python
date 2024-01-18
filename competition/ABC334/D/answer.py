from bisect import bisect_right


def cumulative_sum(arr):
    cumsum = [0]
    for v in arr:
        cumsum.append(cumsum[-1] + v)
    return cumsum


N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

cumsum_R = cumulative_sum(R)
# print(cumsum_R)
for _ in range(Q):
    query = int(input())

    ans = bisect_right(cumsum_R, query)
    print(ans-1)
