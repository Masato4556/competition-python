from math import log10, floor

N = int(input())

digits_num = floor(log10(N+1)) + 1
digits = [0] * digits_num
digits_sum = 0


def add_one(digits, digits_sum):
    digits[0] += 1
    digits_sum += 1

    ind = 0
    while True:
        if digits[ind] < 10:
            break
        digits[ind] = 0
        digits[ind+1] += 1
        ind += 1
        digits_sum -= 9
    return (digits, digits_sum)


ans = 0
for i in range(1, N+1):
    digits, digits_sum = add_one(digits, digits_sum)

    expected = sum(map(int, str(i)))
    if i % digits_sum == 0:
        ans += 1

print(ans)

# 案の定TLE
# N＝10^14なので、各数値ごとに割り切れるか確認する解き方ではだめ
