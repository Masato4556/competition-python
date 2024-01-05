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


def induced_sort(string, buckets, types):
    # 具体的にどのような操作を行なっているかを理解する
    begin_of_bucket = dict([(k, 0) for k in set(string)])
    for _, v in sorted(buckets.items(), key=lambda x: x[0]):
        for elem in v:  # from left to right
            if elem == -1:
                continue  # ignore initialize value
            if types[elem - 1] == 0:  # if the left character is L-type
                buckets[string[elem - 1]
                        ][begin_of_bucket[string[elem - 1]]] = elem - 1
                begin_of_bucket[string[elem - 1]] += 1  # forward current end

    end_of_bucket = dict([(k, len(buckets[k]) - 1) for k in set(string)])
    for k, v in sorted(buckets.items(), key=lambda x: x[0], reverse=True):
        for elem in reversed(v):  # from right to left
            if elem == -1:
                continue
            if types[elem - 1] == 1 and string[elem - 1] != '$':  # if the left character is S-type
                buckets[string[elem - 1]
                        ][end_of_bucket[string[elem - 1]]] = elem - 1
                end_of_bucket[string[elem - 1]] -= 1  # backward current end
    return buckets


def initialize_buckets(s):
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    print(counts)

    buckets = {}
    for c, count in sorted(counts.items()):
        buckets[c] = [-1] * count

    return buckets


def sais(input_str):
    # # int型に変換する
    # s = [ord(c) for c in input_str]
    # s.append(ord("$"))

    s = input_str + "$"

    # Classify charactor to L/S type: S = 1, L = 0 and find LMS
    types, lms_ids = classify_chartype(s)
    print(types, lms_ids)

    # initialize buckets
    buckets = initialize_buckets(s)
    print("init buckets", buckets)

    # LMSを辞書の降順に各バケットの一番下から上へ順に挿入
    end_of_bucket = dict([(s, -1) for s in buckets.keys()])
    print("end_of_bucket", end_of_bucket)
    for lms_id in lms_ids:  # 1)
        pre = s[lms_id]  # prefix of S[lms_ids:]
        print(lms_id, pre)
        buckets[pre][end_of_bucket[pre]] = lms_id
        end_of_bucket[pre] -= 1  # forward current end

    # induced sortを実行する
    print(induced_sort(s, buckets, types))


sais("abracadabra")
