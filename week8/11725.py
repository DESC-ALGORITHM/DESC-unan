import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)  

def DFS(node):
    for i in graph[node]:
        if parent[i] == 0:
            parent[i] = node
            DFS(i)

N = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(N+1)
parent[1] = 1
DFS(1)

for i in range(2, N+1):
    print(parent[i])