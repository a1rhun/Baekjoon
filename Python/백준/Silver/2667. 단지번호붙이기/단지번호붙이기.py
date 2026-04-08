n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

visited = set()
from collections import defaultdict
apart = defaultdict(list)


# 상하좌우를 조사에 쓰일 한 칸 옆 조사
def survey(a, b, x, y):
    if a + x >= 0 and a + x < n and b + y >= 0 and b + y < n:
        return arr[a+x][b+y]
    return -1



# BFS 함수 (단지 리스트에 추가)
def dfs(a, b, idx):
    visited.add((a, b))
    apart[idx].append([a, b])

    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if survey(a, b, i, j) == 1 and (a + i, b + j) not in visited:
            dfs(a+i, b+j, idx)


idx = 0 # 단지
# 전체 탐색 중에 !방문 && 1 인 경우에 대해서 BFS 함수 돌리기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and (i, j) not in visited:
            idx += 1
            dfs(i, j, idx)


# 출력
print(len(apart))

res = list(sorted(len(apart[i + 1]) for i in range(len(apart))))

for i in res:
    print(i)