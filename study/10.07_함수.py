# 정수 N개의 합
def solve(a):
    ans = 0
    for i in a:
        ans = ans + i
    return ans

# 셀프 넘버
def check (i):
    tmp = i
    for j in list(str(i)):
        tmp = tmp + int(j)
    return tmp

lst = []
tmp = 0

for i in range(1,101):
    if i not in lst:
        print(i)
        lst.append(check(i))
    else:
        lst.append(check(i))

# 한수
n = int(input())

cnt = 0
if n < 100:
    print(n)
else:
    for i in range(100,n+1):
        i = list(str(i))
        if (int(i[0])-int(i[1])) == (int(i[1])-int(i[2])):
           cnt = cnt + 1

    print(cnt + 99)


