import sys
from collections import deque

def dfs(graph, start, visited):
    # 현재 노드를 방문처리
    visited[start] = True
    print(start, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N):
    graph[i+1].sort()

visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)
