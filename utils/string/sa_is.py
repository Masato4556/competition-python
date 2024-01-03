# 下記のサイトを参考に自分で実装してみる
# https://gasin.hatenadiary.jp/entry/2017/06/08/101525
# http://shogo82148.github.io/homepage/memo/algorithm/suffix-array/sa-is.html

def classify_chartype(T):
    """ Classify charactor to L/S type: S = 1, L = 0

        Returns
        -------
        :list types: list of 0 and 1
        :list lms_ids: list of Left Most S-type
    """
    num_char = len(T)
    types = [1] * num_char  # S = 1, L = 0
    lms_ids = []
    for i in range(num_char - 2, -1, -1):
        if T[i] > T[i + 1]:  # T[i] is L-type
            types[i] = 0
            if types[i] == 0 and types[i + 1] == 1:
                # position of Left Most S-charactor (LMS)
                lms_ids.append(i + 1)
        elif T[i] == T[i + 1]:
            types[i] = types[i + 1]
    lms_ids.reverse()
    return types, lms_ids


def sais(input_str):
    # int型に変換する
    s = [ord(c) for c in input_str]
    s.append(ord("$"))

    counts = {}
    for c in s:
        print(c)
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    print(counts)

    # initialize buckets
    buckets = {}
    for c, count in sorted(counts.items()):
        print(c, count)
        buckets[c] = [-1] * count

    print(buckets)

    # Classify charactor to L/S type: S = 1, L = 0 and find LMS
    types, lms_ids = classify_chartype(s)
    print(types, lms_ids)

    # induced sortを実行する


sais("banana")
