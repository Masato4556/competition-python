
def shrink(A):
    S = sorted(list(set(A)))
    ranking = {x: i for i, x in enumerate(S)}
    return [ranking[a] for a in A]


A = [4, 90, 25, 30, 30, 8, 90, 90]
print(shrink(A))
