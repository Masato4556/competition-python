def binary_search(arr, target):
    """
    arr: 昇順にソートされた数値の列（リストや配列など）
    target: 探索する数値
    """
    left, right = 0, len(arr) - 1  # 探索範囲の左端と右端
    while left <= right:
        mid = (left + right) // 2  # 探索範囲の中央のインデックス
        if arr[mid] == target:
            return mid  # 探索対象が見つかった場合、そのインデックスを返す
        elif arr[mid] < target:
            left = mid + 1  # 中央より大きい場合、探索範囲を中央より右側にする
        else:
            right = mid - 1  # 中央より小さい場合、探索範囲を中央より左側にする

    # arr中にxが含まれない場合
    # 探索した値と最も近い要素のインデックスを返す
    if left > len(arr) - 1:
        return len(arr) - 1
    elif right < 0:
        return 0
    else:
        return left


N = int(input())
A = list(map(int, input().split()))

S = dict()

sleep_time = 0
for i in range(0, (N-1) // 2):

    S[A[2*i]] = sleep_time
    S[A[2*i+1]] = sleep_time

    sleep_time += A[2*i+2] - A[2*i+1]

S[A[-1]] = sleep_time


Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())

    ri = binary_search(A, r)
    if ri % 2 == 0:
        rt = S[A[ri]] + (r - A[ri])
    else:
        rt = S[A[ri]]

    li = binary_search(A, l)
    if li % 2 == 0:
        lt = S[A[li]] + (l - A[li])
    else:
        lt = S[A[li]]

    print(rt - lt)
