
n = int(input())

words = set(['and', 'not', 'that', 'the', 'you'])

for w in input().split():
    if w in words:
        print("Yes")
        exit()

print("No")