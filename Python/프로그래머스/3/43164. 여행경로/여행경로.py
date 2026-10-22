def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []

    def dfs(airport, path):
        print(path)
        # 종료 조건
        if len(path) == len(tickets)+1:
            return path
        
        for i in range(len(tickets)):
            # 조건: 어떤 티켓을 쓸 수 있을까?
            if not visited[i] and airport == tickets[i][0]:
                visited[i] = True
                result = dfs(tickets[i][1], path+ [tickets[i][1]])
                if result:
                    return result
                else : visited[i] = False
        return None # 실패

    return dfs("ICN", ["ICN"])
