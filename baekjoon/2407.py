n, m = map(int, input().split())

num = 1
for i in range(n, m, -1):
  num *= i
for i in range(1, n-m+1):
  num //= i
print (num)