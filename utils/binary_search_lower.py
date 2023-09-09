# 条件を満たす最も小さい値を見つける
# f: 条件を表す関数。(注意: x未満だったらFalse, x以上だったらTrueになって入る必要がある)
# lo: 探索範囲の下限
# hi: 探索範囲の上限
def binary_search_lower(f, lo, hi):
    left = lo
    right = hi
    assert not f(lo), "探索範囲に境界値が含まれていません"
    assert f(hi), "探索範囲に境界値が含まれていません"

    while right - left > 1:
        mid = (left + right)//2
        if not f(mid):
            left = mid
        else:
            right = mid
    return right

# 説明
# ・ leftは常に条件を満たさな
# ・ rightは常に条件を満たす
# ・ right-left = 1 になるまで範囲を狭める
# ・ right-left = 1 になった際に、rightが条件を満たす最も小さい値になる

# 例: 2乗したら120以上になる最も小さい整数を求める


def f(x):
    # 2乗して120を超えたらTrueを返す関数
    return x**2 > 120


print(binary_search_lower(f, 0, 120))
