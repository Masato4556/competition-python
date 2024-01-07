# zipを利用することで1行で配列を転置できる
def transpose(A):
    return zip(*A)
    # きちんと配列化するなら、list(zip(*A))
