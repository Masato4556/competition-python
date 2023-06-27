# 対象要素のインデックスを返す
def binary_find(arr, target):
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
    return -1  # 探索対象が見つからなかった場合、-1を返す

# 最も近しい値のindexを返す


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
        if target - arr[right] < arr[left] - target:
            return right
        else:
            return left


# 正しく動くか確認していない
# 一致する場合はそのインデックスを、左側のインデックスを返す
def binary_search_left(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


print(binary_find([1, 10, 100], 100))
print(binary_search([1, 10, 100], 5))
