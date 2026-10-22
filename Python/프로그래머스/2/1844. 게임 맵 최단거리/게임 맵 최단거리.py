from collections import deque
# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 길 카운트
def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    q = deque([(0, 0)])
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+ dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and maps[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    

    return dist[n-1][m-1]