import sys
sys.stdin=open("3.txt", "rt")

# 함수파트 

def changesequence(list,a,b):
    nlist = list[b:a-1:-1]
    j = 0
    for i in range(a, b+1):
        list[i]=nlist[j]
        j=j+1

    return list

######## 내부 for문으로 초기화 하기 

# 초기 데이터 

l = list(range(21))


#print(l)
# 입력파트 + 구현파트 

for i in range(10):
    a, b = map(int,input().split())
    changesequence(l, a, b)
    

print(*l[1:])



# 함수파트 


