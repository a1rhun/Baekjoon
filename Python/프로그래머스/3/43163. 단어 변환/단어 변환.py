from collections import deque

def solution(begin, target, words):
    answer = 0
    
    def can_change(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        if count == 1:
            return True
        else : return False
    
    q = deque([(begin, 0)]) # 0은 변경 횟수
    visited = [False] * len(words)
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visited[i] == False and can_change(word, words[i]) == True: # 방문? 기록
                visited[i] = True
                q.append((words[i], cnt + 1))
                
    
      
    
    return answer