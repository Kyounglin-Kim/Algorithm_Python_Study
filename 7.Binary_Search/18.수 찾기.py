# 2021-01-18

# 출처 : https://www.acmicpc.net/problem/1920

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n=int(input())
array1=list(map(int,input().split()))
m=int(input())
array2=list(map(int,input().split()))

array1.sort()
array2

for i in range(m):
    left,right,answer=0,n-1,0
    while left<=right:
        mid = (left+right)//2
        if array1[mid]==array2[i]:
            answer=1
            break
        elif array1[mid]<array2[i]:
            left=mid+1
        else:
            right=mid-1

    print(answer,end='\n')
