from math import factorial, prod


'''
A: 要素の個数の配列
'''
def copunt_permutations(A):
    return factorial(sum(A)) // prod([factorial(a) for a in A]) # (a1+a2+...+an)! / a1!a2!...an!


# 例:白玉2つ、黒玉3つを並べる場合の順列の数を数える[2, 3]
print(copunt_permutations([2, 3]))