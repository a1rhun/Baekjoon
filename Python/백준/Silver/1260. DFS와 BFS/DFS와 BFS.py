N, M, start = map(int, input().split())

node = list(i + 1 for i in range(N)) 

from collections import defaultdict
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for node in graph:
    graph[node].sort()



visited_dfs = set()
dfs_arr = []

def DFS(node):
    visited_dfs.add(node)
    dfs_arr.append(node)

    for i in graph[node]:
        if i not in visited_dfs:
            DFS(i)

bfs_arr = []
from collections import deque

def BFS(s):
    visited = set([s])
    q = deque([start])
    
    while q:
        node = q.popleft()
        bfs_arr.append(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)




DFS(start)
print(*dfs_arr)


BFS(start)
print(*bfs_arr)