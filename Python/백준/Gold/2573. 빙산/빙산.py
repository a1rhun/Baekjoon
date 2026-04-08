import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def melt(land, i, j):
    count = 0
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = i+dx, j+dy
        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 0:
            count += 1
    return count

def next_year(land):
    land_next = [row[:] for row in land]

    for i in range(n):
        for j in range(m):
            if land[i][j] > 0:
                land_next[i][j] = max(0, land[i][j] - melt(land, i, j))

    return land_next


def bfs(start):
    q = deque([start])
    visited = set([start])

    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < m and land[x+dx][y+dy] != 0 and (x+dx, y+dy) not in visited:
                visited.add((x+dx, y+dy))
                q.append((x+dx, y+dy))
    return visited
        

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

# land = next_year(land)

# 1. 생각해야할것 : 분리되었는가?
# 2. 분리된 것을 어떻게 판단할 것인가?
# visited 길이와 현재 land의 빙하 개수를 비교?
# 그래프도 만들어야겠네.. 현재 남아있는거 그래프

year = 0
while True:
    count = 0
    start = None
    for i in range(n):
        for j in range(m):
            if land[i][j] != 0:
                count += 1
                if start == None:
                    start = (i, j)

    if count == 0:
        print(0)
        break

    visited = bfs(start)
    if len(visited) == count:
        land = next_year(land)
        year += 1
    else : 
        print(year)
        break

    
    
