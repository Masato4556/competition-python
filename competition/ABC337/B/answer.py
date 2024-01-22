
S = input()


s_compressed = []
for c in S:
    if len(s_compressed) == 0 or c != s_compressed[-1]:
        s_compressed.append(c)

valid_pattern = {"", "A", "B", "C", "AB", "BC", "AC", "ABC"}

s_compressed = "".join(s_compressed)

print("Yes" if s_compressed in valid_pattern else "No")
