import random
# 1
sports = '축구, 야구, 농구, 배구'.split(', ')
num = [11,9,5,6]

ans = []

for i in range(len(sports)):
    ans.append([sports[i]]+[num[i]])

print(ans)

# 2
ans_2 = []

for i in range(10):
    tmp = random.randint(1,99)
    ans_2.append(tmp)

ans_2.sort()
print(ans_2)

#3
url = 'https://docs.python.org/3/tutorial'
print(url[:url.find(':')])
print(url[url.find('/')+2:url.find('/',url.find('/')+3)])
print(url[url.rfind('/')+1:])

# 4
for i in range(1,10):
    for j in range(1,10):
        print(f'{j} X {i} = {j*i:<2}',end = ' ')
    print()

# 5
data = [[1,2,3],
        [4,5,6],
        [7,8,9]]

lst1 = []
lst2 = []
tmp = 0

for i in range(3):
    for j in range(3):
        tmp = tmp + data[i][j]
    lst1.append(tmp)
    tmp = 0

for i in range(3):
    for j in range(3):
        tmp = tmp + data[j][i]
    lst2.append(tmp)
    tmp = 0

print(f'각 행의 합: {lst1}')
print(f'각 행의 합: {lst2}')

# 6
m = [[1,2],[3,4],[5,6],[7,8]]

print('원행렬(m) 출력')
for i in m:
    for j in i:
        print(j, end = ' ')
    print()

print('전치행렬 출력')
for i in range(len(m[0])):
    for j in m:
        print(j[i], end = ' ')
    print()