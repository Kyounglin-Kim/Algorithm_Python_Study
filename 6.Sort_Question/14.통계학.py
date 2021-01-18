# 2021-01-14

# 출처 : https://www.acmicpc.net/problem/2108

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#

import sys
input = sys.stdin.readline

n=int(input())

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()

# 산술평균
print('%.f' %(sum(array)/n))

# 중앙값

# 2) 중앙값 구하기

# def median(array):
#     if len(array)==1:
#         return(array[0])
#
#     elif len(array)%2!=0:
#         index=int((len(array)+1)/2)
#         return(array[index]-1)
#     else:
#         index1=int(len(array)/2)
#         index2=int(len(array)/2+1)
#
#         median_mean=(array[index1-1]+array[index2-1])/2
#         return('%.f' % median_mean)
#
#
# print(median(array))

print(array[n//2])


# 3) 최빈값 출력

from collections import Counter

cnt=Counter(array).most_common()

if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

else:
    print(array[0])


# 4) 범위 출력
print(array[-1]-array[0])

