# 連続する要素を(値、個数)で表すことで圧縮する手法

from itertools import groupby


def run_length_encoding(a):
    return [(k, len(list(g))) for k, g in groupby(a)]

# これを用いてACできる問題 127D

# 参考
# https://output-zakki.com/run_length_encoding/
