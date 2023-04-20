# 昇順にソートした際に、元の配列のインデックスがどこに移動したかを表す配列を返す

arr = [0, 3, 4, 2, 1]

inds = [i[0] for i in sorted(enumerate(arr), key=lambda x:x[1])]

print(arr)
print(inds)