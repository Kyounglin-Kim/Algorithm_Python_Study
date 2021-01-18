# 2021-01-11

# 출처 : https://www.acmicpc.net/problem/1260

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

n,m,v=map(int,input().split())
array=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    array[x][y]=array[y][x]=1

visited=[0]*(n+1)

def dfs(v):
    visited[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if(visited[i]==0 and array[v][i]==1):
            dfs(i)


def bfs(v):
    queue=[v]
    visited[v]=0
    while queue:
        v=queue.pop(0)
        print(v,end=' ')
        for i in range(1,n+1):
            if(visited[i]==1 and array[v][i]==1):
                queue.append(i)
                visited[i]=0



dfs(v)
print()
bfs(v)