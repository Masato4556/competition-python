
T = int(input())


for _ in range(T):
    N, K = map(int, input().split())
    S = input()

    # はじめに出てくる"１"のインデックスを取得
    first_one = -1 
    con_q_max_len = 0
    con_q_max_len_cnt = 0
    con_q_len = 0
    for i in range(N):
        if S[i] == "1":
            first_one = i
            break
        elif S[i] == "?":
            con_q_len += 1
        else:
            if con_q_len > con_q_max_len:
                con_q_max_len = max(con_q_max_len, con_q_len)
                con_q_max_len_cnt = 1
            elif con_q_len == con_q_max_len:
                con_q_max_len_cnt += 1
            con_q_len = 0
    if con_q_len > con_q_max_len:
        con_q_max_len = max(con_q_max_len, con_q_len)
        con_q_max_len_cnt = 1
    elif con_q_len == con_q_max_len:
        con_q_max_len_cnt += 1
    
    # 1が存在しないなら、”No”
    if first_one == -1:
        if con_q_max_len == K and con_q_max_len_cnt == 1:
            print("Yes")
        else:
            print("No")
        continue
    
    # 最後に出てくる"１"のインデックスを取得
    last_one = -1 
    for i in range(N-1, -1, -1):
        if S[i] == "1":
            last_one = i
            break

    # "1"に挟まれた"0"が存在するなら、"No"
    flg = False
    for i in range(first_one+1, last_one):
        if S[i] == "0":
            flg = True
            break
    if flg:
        print("No")
        continue

    num_one = last_one-first_one+1
    if num_one == K:
        print("Yes")
        continue
    elif num_one > K:
        print("No")
        continue    
    
    # はじめに出てくる"1"の左側に隣接している連続している"?"の個数
    num_q_l = 0
    for i in range(first_one-1, -1, -1):
        if S[i] != "?": break
        num_q_l += 1
    
    # 最後に出てくる"1"の右側に隣接している連続している"?"の個数
    num_q_r = 0
    for i in range(last_one+1, N):
        if S[i] != "?": break
        num_q_r += 1
    
    if num_one + num_q_l + num_q_r == K:
        print("Yes")
        continue
    elif num_one + num_q_l + num_q_r > K:
        if num_q_l == 0 or num_q_r == 0:
            print("Yes")
            continue
    
    print("No")
