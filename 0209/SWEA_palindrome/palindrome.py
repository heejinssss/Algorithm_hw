'''
Q. 8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수 구하기

행/열별로 제시된 길이(N)만큼의 구간을 글자판 범위 안에서 반복 탐색
'''


# T = int(input())
T = 10

for test_case in range(1, T + 1):

    N = int(input())
    arr = []
    cnt = 0 # 회문 개수

# input 값을 각 원소별로 저장
    for _ in range(8):
        a = list(map(str, input().split()))
        arr.append(a[0])

# 행 기준으로 찾기
    for i in range(8):
        for k in range(8-N+1):
            if arr[i][k:N+k] == (arr[i][k:N+k])[::-1]: # 회문이면
                cnt += 1

# 열 기준으로 찾기
    for j in range(8):
        cache = []
        for i in range(8):
            cache.append(arr[i][j])
        for k in range(8-N+1):
            if cache[k:N+k] == (cache[k:N+k])[::-1]: # 회문이면
                cnt += 1

    print(f'{test_case} {cnt}')