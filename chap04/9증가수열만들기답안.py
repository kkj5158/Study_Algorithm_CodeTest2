import sys
sys.stdin=open("chap04/9.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
lt = 0 
rt = n-1
last = 0
res = ""
tmp = []

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break

