def get_alphabet(i):
    """
    i: int, アルファベットの位置を表す数値(1から26までの整数)
    return: str, i番目のアルファベットを表す文字列
    """
    # ASCIIコードを使ってi番目のアルファベットを取得する
    # 小文字を取得する場合は、ord('a')を基準に加算する
    return chr(ord('a') + i - 1)