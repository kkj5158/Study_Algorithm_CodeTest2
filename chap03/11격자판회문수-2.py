import sys
sys.stdin=open("chap03/11.txt", "rt")

mp = [list(map(int, input().split())) for _ in range(7)]


def isrotate(x):
    nlist = x[::-1]
    if nlist==x:
        return True
    else:
        return False


    

"""
for x in mp:
    print(x)
0
"""




"""

회문의 크기가 3인경우 
회문의 크기가 4인경우
회문의 크기가 5인경우 
회문의 크기가 6인경우
회문의 크기가 7인경우

--> 아니면 리스트의 인덱싱 기능을 사용하여서 회문의 수 구하기 ? 
(회문 체크 알고리즘은 하나로 )

회문이 행에 존재하는 경우


회문이 열에 존재하는 경우 

회문의 판별을 리스트의 기능을 빌려오지 않고서 구현하는 경우는 ?????

map 의 하나하나의 원소를 기준으로 인덱스 비교 연산을 구현하는 경우는 ?>> 


"""
cnt = 0

for n in range(3,8):
    for i in range(7):
        for j in range(7):
            while True:
                first = i+0
                second = j+n-1
                if mp[first][second] == mp[first][second]:
                    

            
    


"""
->> 이런 접근 방식은 열에서의 회문의 갯수를 구할때 너무 적절하지 않다. 원소하나하의 기준으로 알고리즘을 구현해보자. 

"""