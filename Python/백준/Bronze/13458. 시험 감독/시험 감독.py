import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for i in A:
    tmp = i - B
    cnt += 1
    if tmp > 0:
        cnt += math.ceil(tmp / C)


print(cnt)

