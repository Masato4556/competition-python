"""
文字列 S が与えられたときに、各 i について
「文字列S[0,i-1]の接頭辞と接尾辞が最大何文字一致しているか」を記録した配列を作成するアルゴリズム。

※ 注意
接頭辞と接尾辞が全く同じ部分文字列(S[i,j])になった場合は、一致していないものとして見做す。
例:
  "a" => 0文字一致とみなす。
  "aa" => 1文字一致とみなす。（接頭辞 S[0,0], 接尾辞 S[1,1]）
  "aaa" => 2文字一致とみなす。（接頭辞 S[0,1], 接尾辞 S[1,2]）

計算量O(|S|)

参考
https://snuke.hatenablog.com/entry/2014/12/01/235807
"""


def mp(S):
    A = [-1] * (len(S)+1)
    j = -1
    for i in range(len(S)):
        print(S, S[0:i+1] if i >= 1 else "_" )
        print("s", i, j, A)

        while j >= 0 and S[i] != S[j]:
            j = A[j]
            print("r", i, j, A)
        j += 1
        A[i+1] = j
        print("e", i, j, A)

    return A


print(mp("aaabaabaaa"))

"""
TODO:
- KMP法の実装をしてみる
- これらのアルゴリズムをどのように利用するのか理解する(文字列検索、周期生の判定など)


"""