# 최소 최대
N = int(input())
a = list(map(int, input().split(' ')))

print(min(a), end = ' ')
print(max(a))

# 최댓값
lst = []
for i in range(9):
    lst.append(int(input()))

m = max(lst)
print(m)
print(lst.index(m)+1)

# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

ans = list(str(a*b*c))

for i in range(10):
    print(ans.count(str(i)))

# 나머지
lst = []
for i in range(10):
    lst.append((int(input()))%42)
lst = set(lst)
print(len(lst))

# 평균
N = int(input())
score = list(map(int,input().split(' ')))
M = max(score)
# avg = sum(score)/N
# avg = avg/M*100
print(sum(score)/N/M*100)

# OX퀴즈
n = int(input())
lst = []
tmp = 0
score = 0
for i in range(n):
    lst.append(list(input()))

for i in lst:
    for j in i:
        if j == 'O':
            tmp = tmp + 1
            score = score + tmp
        else:
            tmp = 0
    print(score)
    score = 0
    tmp = 0

# 평균은 넘겠지
n = int(input())
lst = []
cnt = 0

for i in range(n):
    lst.append(list(map(int,input().split(' '))))\

for i in lst:
    avg = sum(i[1:])/i[0]
    for j in i[1:]:
        if j > avg:
            cnt = cnt + 1
    print(f'{(cnt/i[0]*100):.3f}%')
    avg = 0
    cnt = 0








