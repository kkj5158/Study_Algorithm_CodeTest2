
n = int(input())

members = []

for _ in range(n):
    members.append(list(map(int,input().split())))

#print(a)

cnt = 0
check = 0


for i in range(len(members)):
    h, k = map(int , members[i])
    check = 0
    for m in members:
        if h < m[0] and k < m[1]:
            check = 1
            continue
    if check == 0:
        cnt += 1

print(cnt)
