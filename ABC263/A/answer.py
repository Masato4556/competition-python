from collections import defaultdict

a = list()
cnt = defaultdict(int)

for v in map(int, input().split()):
    cnt[v] += 1

cnt_list = list(cnt.values())
cnt_list.sort()

if cnt_list[0] == 2 and cnt_list[1] == 3:
    print("Yes")
else:
    print("No")
