from itertools import groupby
A_rl = [(k, len(list(g))) for k, g in groupby(A)]