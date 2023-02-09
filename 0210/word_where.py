'''
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1

2

N : N*N 배열
K : 단어 길이
0 : 검은색
1 : 흰색
'''

# arr = []

# for _ in range(N):
#     arr.append(list(map(int, input().split())))

arr = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]

N = 5
K = 3

cnt = 0

for i in range(N):
    cnt_one = 0
    for j in range(N):
        if cnt_one == K:
            cnt += 1
            continue
        if arr[i][j] == 1: # 1을 발견하면 cnt_one + 1
            cnt_one += 1
        if arr[i][j] == 0: # 연속이 끊기면 cnt_one = 0
            cnt_one = 0

for j in range(N):
    cnt_one = 0 # 0의 개수가 단어 길이와 일치하는 행 또는 열
    for i in range(N):
        if cnt_one == K:
            cnt += 1
            continue
        if arr[i][j] == 1: # 1을 발견하면 cnt_one + 1
            cnt_one += 1
        if arr[i][j] == 0: # 연속이 끊기면 cnt_one = 0
            cnt_one = 0

print(cnt)