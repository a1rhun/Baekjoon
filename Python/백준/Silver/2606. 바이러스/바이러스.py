from collections import defaultdict
n = int(input()) # 노드의 수
m = int(input()) # 그래프 수

node = list(i + 1 for i in range(n))

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = []
visited = set()

def dfs(node):
    visited.add(node)
    res.append(node)

    for next_node in graph[node]:
        if next_node not in visited:
            visited.add(next_node)
            dfs(next_node)

dfs(1)
print(len(res) - 1)
            

    