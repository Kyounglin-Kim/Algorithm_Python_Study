# 2021-01-15

# 출처 : https://www.acmicpc.net/problem/1181

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

n=int(input())
array=[]

for _ in range(n):
    a=input()
    array.append((a,len(a)))

array=set(array)
array=list(array)
array.sort(key=lambda x: (x[-1],x[0]))

answer=[x for x,y in array]

for j in answer:
    print(j,end='\n')



# final=[]
# for i in range(len(answer)):
#     if i==len(answer)-1:
#         final.append(answer[i])
#
#     elif answer[i]==answer[i+1]:
#         pass
#
#     else:
#         final.append(answer[i])
#
# for j in final:
#     print(j,end='\n')


