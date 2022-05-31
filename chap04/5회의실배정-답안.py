# 회의가 끝나는 시간으로 정렬을 해나간다. 

import sys
sys.stdin=open("chap04/5.txt", "rt")

n = int(input())

meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1], x[0]))

# x[1] -> end 타임이 첫번째 우선순위에, x[0] 가 두번째 우선순위가 되어라 

"""
for x in meeting:
    print(x)
"""

et = 0

cnt= 0

for s, e in meeting:
    if s>=et:
        et=e
        cnt += 1
    
print(cnt)

