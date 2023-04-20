import bisect

def calc_lis_len(seq):
    lis = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > lis[-1]:
            lis.append(seq[i])
        else:
            lis[bisect.bisect_left(lis, seq[i])] = seq[i]

    return len(lis)

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

inds = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1])]

print(calc_lis_len([A[i] for i in inds]) + calc_lis_len([B[i] for i in inds]))
