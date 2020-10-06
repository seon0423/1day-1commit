import sys

# 구구단
n = int(input())

for i in range(1,10):
    print(f'{n} * {i} = {n*i}')

# A+B-3
n = int(input())

for i in range(n):
    A,B = map(int,input().split(' '))
    print(A+B)

# 합
n = int(input())
sum = 0

for i in range(1,n+1):
    sum = sum + i

print(sum)

# 빠른 A+B
T = int(sys.stdin.readline())

for i in range(T):
    A,B = map(int,sys.stdin.readline().split(' '))
    print(A + B)

# N 찍기
N = int(input())

for i in range(1,N+1):
    print(i)

# 기찍 N
N = int(input())

for i in range(N,0,-1):
    print(i)

# A + B -7
T = int(input())

for i in range(T):
    a,b = map(int,input().split(' '))
    print(f'Case #{i+1}: {a+b}')

# A + B -8
T = int(input())

for i in range(T):
    a,b = map(int,input().split(' '))
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

# 별찍기 -1
N = int(input())

for i in range(1,N+1):
    print('*'*i)

# 별찍기 -2
N = int(input())

for i in range(1,N+1):
    print(f'{" "*(N-i)}{"*"*i}')

# X보다 작은 수
N,X = map(int,input().split(' '))
A = list(map(int, input().split(' ')))

for i in A:
    if i<X:
        print(i, end=' ')

# 달달함이 넘쳐흘러
a = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))

print(c[0]-a[-1], end = ' ')
print(int(c[1]/a[-2]), end = ' ')
print(c[2]-a[-3], end = ' ')