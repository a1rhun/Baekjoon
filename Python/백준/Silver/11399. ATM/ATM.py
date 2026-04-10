n = int(input())

arr = list(map(int, input().split()))
arr.sort()


sum = 0
cnt = n
for i in range(n):
    sum += arr[i] * (cnt - i)

print(sum)