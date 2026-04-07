n = int(input())
f = 1
for _ in range(n): 
    f = f * n
    n = n - 1


arr = str(f)
arr = ''.join(reversed(arr))


for i in range(len(arr)):
    if arr[i] == '0':
        continue
    else : 
        print(i) 
        break


import math
n = int(input())
f = str(math.factorial(n))
print(len(f) - len(f.rstrip('0')))