

#DFS 
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [], 5: [], 6: []
}

visited = set()  # 방문한 노드 기록 (중복 방지)

def dfs(node):
    visited.add(node)
    print(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)

dfs(1)

def dfs_stack(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for next_node in graph[node]:
            if next_node not in visited:
                stack.append(next_node)

# #BFS
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [], 5: [], 6: []
}

def bfs(start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        print(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)

bfs(1)


def bfs_distance(start, end):
    visited = set([start])
    queue = deque([(start, 0)]) # 노드, 거리

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist+1))

    return -1 # 도달 불가


# 2D 그리드 BFS
from collections import deque

# 상하좌우
# i = 0 : 위, i = 1 : 아래... 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

def bfs_grid(grid, start_x, start_y):
    n = len(grid) # 4
    m = len(grid[0]) # 4

    visited = [[False] * m for _ in range(n)]

#     visited = [
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False]
# ]

    visited[start_x][start_y] = True

    queue = deque([(start_x, start_y, 0)]) # 행, 열, 거리

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크 + 벽 + 방문 체크
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))