# # 두 수 비교하기
# a, b = map(int, input().split(' '))
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')
#
# # 시험성적
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')
#
# # 윤년
# year = int(input())
#
# a = year % 4
# b = year % 100
# c = year % 400
#
# if a == 0 and b != 0:
#     print('1')
# elif a == 0 and c == 0:
#     print('1')
# else:
#     print('0')

year = int(input())

a = year % 4
b = year % 100
c = year % 400

if a == 0:
    if (b != 0) or (c == 0):
        print('1')
else:
    print('0')

# 사분면 고르기
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
else:
    print('4')

# 알람시계
H, M = map(int,input().split(' '))

if M >= 45:
    M = M - 45
else:
    if H == 0:
        H = 23
    else:
        H = H -1
    M = 60 + M - 45    # 60-(45-M)

print(H, M)