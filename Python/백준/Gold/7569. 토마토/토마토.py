import sys
input = sys.stdin.readline

from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split()))for _ in range(N)] for _ in range(H)]

# 010 0-10 100 -100 001 00-1
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                q.append((z, x, y))
            




while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
        if 0<=nz<H and 0<=nx<N and 0<=ny<M and box[nz][nx][ny] == 0:
            box[nz][nx][ny] += box[z][x][y] + 1
            q.append((nz, nx, ny))

res = 0
found_zero = False

for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 0:
                found_zero = True
            else : res = max(res, box[z][x][y])


if found_zero:
    print(-1)
else: print(res -1)