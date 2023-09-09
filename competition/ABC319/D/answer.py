# 条件を満たす最も小さい値を見つける
# f: 条件を表す関数。x未満だったらFalse, x以上だったらTrueになるようにする。
# lo: 探索範囲の下限
# hi: 探索範囲の上限
def binary_search_lower(f, lo, hi):
    left = lo
    right = hi

    while right - left > 1:
        mid = (left + right)//2
        if not f(mid):
            left = mid
        else:
            right = mid
    return right


N, M = map(int, input().split())
L = list(map(int, input().split()))


def f(w):
    cur_w = 0
    line = 1
    for l in L:
        if cur_w + l > w:
            line += 1
            cur_w = 0
        cur_w += l+1
    return line <= M


print(binary_search_lower(f, max(L)-1, sum(L) + N))
