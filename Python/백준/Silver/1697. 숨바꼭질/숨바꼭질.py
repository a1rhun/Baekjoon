from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 딕셔너리에??? 

def bfs(start, end):
    if start == end:
        return 0
    visited = set()
    visited.add(start)
    q = deque([start])
    node_depth = {start:0}
    node_depth[start] = 0
    cnt = 0

    while q:
        node = q.popleft()

        for i in [node - 1, node + 1, 2 * node]:
            if i not in visited and 0 <= i <= 100000:
                visited.add(i)
                q.append(i)
                node_depth[i] = node_depth[node] + 1
                if i == end:
                    return node_depth[i]
                

print(bfs(N, K))