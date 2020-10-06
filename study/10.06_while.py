import sys
# A + B - 5
while ' ':
    a,b = map(int, input().split(' '))
    if a ==0 and b == 0:
        break
    else:
        print(a+b)

# A + B -4
while True:
    try:
        a,b = map(int,input().split(' '))
        print(a+b)
    except:
        break
import sys

# 더하기 사이클
n = int(input())
n1 = n
ans = 0
while True:
    tmp = (n%10)+(n//10)
    n = n%10*10+tmp%10
    ans = ans + 1
    if n1 == n:
        print(ans)
        break