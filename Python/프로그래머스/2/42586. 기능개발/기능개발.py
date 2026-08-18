# 100 되면 pop 후 count 배포
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses :
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        if count != 0:
            answer.append(count)
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
            
    return answer