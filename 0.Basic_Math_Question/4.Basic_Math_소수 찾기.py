# 2021-01-05

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())
array=list(map(int,input().split()))

count=0

for i in array:
    check=[]
    for j in range(1,i+1):
        if i%j==0:
            check.append(i)
    if len(check)==2:
        count+=1

print(count)



