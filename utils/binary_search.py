def binary_search(arr, target):
    """
    arr: 昇順または降順にソートされた数値の列（リストや配列など）
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
