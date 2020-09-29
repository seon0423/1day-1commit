# def solution(numbers, hand):
#     # * 은 10, 0은 11, #은 12라 가정
#     answer = ''
#     r = 10
#     l = 12
#     for j in range(len(numbers)):
#         if numbers[j] == 0:
#             numbers[j] = 10
#
#     for i in numbers:
#         if i % 3 == 0:
#             r = i
#             answer = answer + 'R'
#         elif i % 3 == 1:
#             l = i
#             answer = answer + 'L'
#         elif i % 3 == 2:
#             r_cor = divmod(r,3)
#             l_cor = divmod(l,3)
#             next = divmod(i,3)
#             r_dis = abs(r_cor[0]-next[0])+abs(r_cor[1]-next[1])
#             l_dis = abs(l_cor[0] - next[0]) + abs(l_cor[1] - next[1])
#             print(f'r_dis = {r_dis}, l_dis = {l_dis}')
#             if r_dis < l_dis:
#                 r = i
#                 answer = answer + 'R'
#             elif r_dis > l_dis:
#                 l = i
#                 answer = answer + 'L'
#             elif hand == 'right':
#                 r = i
#                 answer = answer + 'R'
#             else:
#                 l = i
#                 answer = answer + 'L'
#             print(f'r = {r}, l = {l}')
#     return answer

def solution(numbers, hand):
    tmp = 1
    keypad = dict()
    r = 10
    l = 12
    answer = ''
    for i in range(4):
        for j in range(3):
            keypad[tmp] = (i,j)
            tmp = tmp + 1
    for j in range(len(numbers)):
        if numbers[j] == 0:
            numbers[j] = 11

    for i in numbers:
        if i % 3 == 0:
            r = i
            answer = answer + 'R'
        elif i % 3 == 1:
            l = i
            answer = answer + 'L'
        elif i % 3 == 2:
            r_dis = abs(keypad[r][0]-keypad[i][0]) + abs(keypad[r][1]-keypad[i][1])
            l_dis = abs(keypad[l][0] - keypad[i][0]) + abs(keypad[l][1] - keypad[i][1])
            if r_dis < l_dis:
                r = i
                answer = answer + 'R'
            elif r_dis > l_dis:
                l = i
                answer = answer + 'L'
            elif hand == 'right':
                r = i
                answer = answer + 'R'
            else:
                l = i
                answer = answer + 'L'
            print(f'r = {r}, l = {l}')
    return answer




numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = 'right'

print(solution(numbers, hand))