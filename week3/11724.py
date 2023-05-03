import sys

sys.setrecursionlimit(100000)

N, M = map(int, sys.stdin.readline().rstrip().split())

def dfs(x:int, y:int) -> bool:
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

graph = [[0] * M for _ in range(N)]

result = 0
for _ in range(N):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[v][u] = 1
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1
    print(result)
