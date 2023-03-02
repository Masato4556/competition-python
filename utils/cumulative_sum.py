
# 累積和
# cumsum[i]は、インデックス0からインデックスiまでの数値を合計した値
# cumsum[0]は範囲に何も要素がないため、必ず0になる
def cumulative_sum(array):
    """
    array: リストや配列などの数値の列
    """
    n = len(array)
    cumsum = [0] * (n+1)
    for i in range(n):
        cumsum[i+1] = cumsum[i] + array[i]
    return cumsum

print(cumulative_sum([0,1,2,3,4,5,6,7,8,9,10]))