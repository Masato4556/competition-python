import bisect

#リストseqからLISの長さを出す
def calc_lis_len(seq):
    lis = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > lis[-1]:
            lis.append(seq[i])
        else:
            lis[bisect.bisect_left(lis, seq[i])] = seq[i]

    return len(lis)


'''
下記のQiita記事からコードをコピーしただけなので、
ちゃんと内容を読んで理解する。
https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
```