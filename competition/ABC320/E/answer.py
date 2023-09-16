# 2分探索を利用した回答
# TLEで突破ならず

def binary_search_lower(f, lo, hi):
    left = lo
    right = hi
    if f(lo):
        return lo
    if not f(hi):
        return -1

    while right - left > 1:
        mid = (left + right)//2
        if not f(mid):
            left = mid
        else:
            right = mid
    return right


N, M = map(int, input().split())

events = [list(map(int, input().split())) for _ in range(M)]
events.sort()

events_done = [False for _ in range(M)]
ans = [0 for _ in range(N)]


def gen_f(next_time):
    return lambda i: next_time <= events[i][0]


for i in range(N):
    next_time = 0
    next_event_i = binary_search_lower(gen_f(next_time), 0, M-1)
    while next_event_i != -1:
        while next_event_i < M and events_done[next_event_i]:
            next_event_i += 1

        if next_event_i >= M:
            break

        t, w, s = events[next_event_i]
        ans[i] += w
        next_time = t+s
        events_done[next_event_i] = True
        next_event_i = binary_search_lower(gen_f(next_time), 0, M-1)

for a in ans:
    print(a)
