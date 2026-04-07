n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
T = [s[0] for s in schedule]
P = [s[1] for s in schedule]

dp = [0] * (n + 2)

for i in range(n - 1, -1, -1):
    if i + T[i] <= n:
        # dp[i + T[i]] : 선택했을 때, 그 다음 날 의 최선과의 합
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i + 1]

print(dp[0])