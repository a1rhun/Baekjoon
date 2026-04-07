

def print_board(arr):
    for row in arr:
        print(''.join(row))

# 현재 row, column, 움직일 row, col
def move(r, c, dr, dc):
    while board[r + dr][c + dc] != '#':
        r += dr
        c += dc
        if board[r][c] == 'O':
            break
    return r, c

def tilt(rr, rc, br, bc, dr, dc):
    rr2, rc2 = move(rr, rc, dr, dc)
    br2, bc2 = move(br, bc, dr, dc)

    if rr2 == br2 and rc2 == bc2 and board[rr2][rc2] != 'O':
        # 앞에 있던게 우선, 뒤에 있는건 미루기
        if dr == 1: 
            if rr > br: br2 = rr2 -1
            else : rr2 = br2 - 1
        elif dr == -1:
            if rr < br: br2 = rr2 + 1
            else: rr2 = br2 + 1
        elif dc == 1:
            if rc > bc : bc2 = rc2 - 1
            else: rc2 = bc2 - 1
        elif dc == -1:
            if rc < bc: bc2 = rc2+ 1
            else: rc2 = bc2 + 1
    return rr2, rc2, br2, bc2


# board = [
#     list("#####"),
#     list("#..B#"),
#     list("#.#.#"),
#     list("#RO.#"),
#     list("#####"),
# ]

# # 초기 위치.
# rrr = len(board)
# ccc = len(board[0])
# for r in range(rrr):
#     for c in range(ccc):
#         if board[r][c] == 'R':
#             rr, rc = r, c
#         elif board[r][c] == 'B':
#             br, bc = r, c

# print(f"R: ({rr}, {rc}), B: ({br}, {bc})")
# dirs = [(1, 0, '아래'), (-1, 0, '위'), (0, 1, '오른쪽'), (0, -1, '왼쪽')]
# for dr, dc, name in dirs:
#     rr2, rc2, br2, bc2 = tilt(rr, rc, br, bc, dr, dc)
#     print(f"{name} -> R : ({rr2}, {rc2}), B : ({br2}, {bc2})")


from collections import deque
def bfs(rr, rc, br, bc):
    # 초기 상태 (rr, rc, br, bc, dist)
    queue = deque([(rr, rc, br, bc, 0)])
    visited = set()
    visited.add((rr, rc, br, bc))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue: 
        rr, rc, br, bc, cnt = queue.popleft()

        if cnt >= 10:
            break

        for dr, dc in dirs:
            rr2, rc2, br2, bc2 = tilt(rr, rc, br, bc, dr, dc)

            # 파란 구슬 빠짐
            if board[br2][bc2] == 'O':
                continue
            # 빨간 구슬만 빠짐 -> 정답
            if board[rr2][rc2] == 'O':
                return cnt + 1
            
            # 방문햇음
            if (rr2, rc2, br2, bc2) in visited:
                continue

            visited.add((rr2, rc2, br2, bc2))
            queue.append((rr2, rc2, br2, bc2, cnt + 1))
    return -1


from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            rr, rc = r, c
        elif board[r][c] == 'B':
            br, bc = r, c

print(bfs(rr, rc, br, bc))