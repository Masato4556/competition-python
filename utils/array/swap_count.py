
# 隣り合う要素を入れ替えてソートする場合の手数を求める関数
# ABC332Dで利用
def min_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1

    return swap_count
