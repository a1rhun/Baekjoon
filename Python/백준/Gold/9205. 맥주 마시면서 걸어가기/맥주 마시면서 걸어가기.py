def distance(nx, ny, dx, dy): # now, dist
    return abs(dx - nx) + abs(dy - ny)

def dfs(start):
    visited.add(start)

    for next_node in graph[start]:
        if next_node not in visited:
            dfs(next_node)

# 편의점 들르면 맥주 20으로 복귀
# 결국 1키로만 이동 가능
# 1키로 반경 내에 있는건 결국 그래프!!!! 
# DFS 진행해서 만약 dest에 도착 시, 함수 종료 및 happy 출력 
# dest 도착한 것은 visited로 판단
# 그럼 일단 그래프 화를 먼저 시키자. 

tc = int(input())
for i in range(tc):
    n = int(input()) 
    house = list(map(int, input().split()))
    store = [list(map(int, input().split()))for i in range(n)]
    dest = list(map(int, input().split()))

    # 그래프 만들기
    from collections import defaultdict
    graph = defaultdict(list)

    store.append(house)
    store.append(dest)
    store.sort()

    for (a, b) in store:
        for (c, d) in store:
            if distance(a, b, c, d) <= 1000 and distance(a, b, c, d) > 0:
                graph[(a, b)].append((c, d))

    tuple_house = (house[0], house[1])
    dest = (dest[0], dest[1])

    visited = set()
    dfs(tuple_house)

    if dest in visited:
        print('happy')
    else: print('sad')