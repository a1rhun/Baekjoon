from collections import deque

# 그래프 만드는 함수
# 네트워크 개수 세는 함수 (dfs)

def solution(n, computers):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and visited[i] == False:
                dfs(i)
                

    answer = 0
    for i in range(n):
        if visited[i] == False:
            answer += 1
            dfs(i)
            
    return answer