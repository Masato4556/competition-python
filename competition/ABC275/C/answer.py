
pawn_pos_list = []
for i in range(9):
    s = input()
    for j in range(9):
        if s[j] == ".": continue
        pawn_pos_list.append((i+1, j+1))

l = len(pawn_pos_list)

square_set = set()
for i in range(l):
    r_1, c_1 = pawn_pos_list[i]
    for j in range(i+1, l):
        r_2, c_2 = pawn_pos_list[j]
        dist_12_r, dist_12_c = r_2 - r_1, c_2 - c_1

        if dist_12_c > 0:
            r_3, c_3 = r_1 + (dist_12_c), c_1 - (dist_12_r)
            r_4, c_4 = r_3 + (dist_12_r), c_3 + (dist_12_c)
        else:
            r_3, c_3 = r_1 - (dist_12_c), c_1 + (dist_12_r)
            r_4, c_4 = r_3 + (dist_12_r), c_3 + (dist_12_c)
        if (r_3, c_3) in pawn_pos_list and (r_4, c_4) in pawn_pos_list :
            square_pos = [(r_1, c_1), (r_2, c_2), (r_3, c_3), (r_4, c_4)]
            square_pos.sort()
            square_set.add(tuple(square_pos))
        
        
print(len(square_set))