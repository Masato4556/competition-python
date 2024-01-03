def build_suffix_array(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]


def search_pattern(suffix_array, T, P):
    low, high = 0, len(suffix_array) - 1

    while low <= high:
        mid = (low + high) // 2

        suffix_start = suffix_array[mid]
        suffix = T[suffix_start:]

        if P == suffix[:len(P)]:
            # Match found, check for other occurrences
            occurrences = [suffix_start]

            # Check left
            i = mid - 1
            while i >= 0 and P == T[suffix_array[i]:suffix_array[i] + len(P)]:
                occurrences.append(suffix_array[i])
                i -= 1

            # Check right
            # info: slicing outside the bounds of a sequence doesn't cause an error.
            i = mid + 1
            while i < len(suffix_array) and P == T[suffix_array[i]:suffix_array[i] + len(P)]:
                occurrences.append(suffix_array[i])
                i += 1

            return occurrences

        elif P < suffix[:len(P)]:
            high = mid - 1
        else:
            low = mid + 1

    return []


def find_pattern_positions(T, P):
    suffix_array = build_suffix_array(T)
    positions = search_pattern(suffix_array, T, P)
    return positions


# Example usage:
T = "banana"
P = "anan"
positions = find_pattern_positions(T, P)
print(f"The pattern '{P}' occurs at positions: {positions}")

'''
TODO:

suffix arrayのソートの処理でO(T^2logT)と計算量が膨らんでいるので、下記の記事を見て2段階の高速化を理解して実装してみる
https://gasin.hatenadiary.jp/entry/2017/06/08/101525

1. Manber&Myers algorithm O(Tlog^2_T)

2. SA-IS O(T)

SA-ISに関しては下記の記事が参考になりそう
下記の記事などを参考にSA ISを用いて計算量を削減する
https://trap.jp/post/953/
'''
