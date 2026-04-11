import sys
input = sys.stdin.readline
from collections import deque

def find_dest(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return i, j


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


dx, dy = find_dest(arr)


def cal(arr, dx, dy):
    res = []
    res = [[-1] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                res[i][j] = 0  # 미리 벽 처리
    res[dx][dy] = 0
    q = deque()
    q.append((dx, dy))

    while q:
        cx, cy = q.popleft()
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if cx + x >= 0 and cx + x < N and cy + y >= 0 and cy + y < M:
                if arr[cx+x][cy+y] == 1 and res[cx+x][cy + y] == -1:
                    res[cx+x][cy+y] = res[cx][cy] + 1
                    q.append((cx+x, cy+y))
    return res

res = cal(arr, dx, dy)

for row in res:
    print(*row)