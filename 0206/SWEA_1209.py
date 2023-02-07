'''
Q. 100X100 2차원 배열의 행별, 열별, 대각선 원소의 합 중 최대값 구하기

각 행별, 열별, 대각선 원소별로 합을 구한 뒤 max 값 추출
'''

T = 10
 
for test_case in range(1, T + 1):
    tc = int(input())
    _arr = [list(map(int, input().split())) for _ in range(100)]
 
    N = len(_arr)
 
    _max = []
    _fin = []
 
    # 행별로
    for i in range(N):
        for j in range(N):
            _max.append(_arr[i][j])
        _fin.append(sum(_max))
        _max.clear()
 
    # 열별로
    for j in range(N):
        for i in range(N):
            _max.append(_arr[i][j])
        _fin.append(sum(_max))
        _max.clear()

    # 대각선
    for i in range(N):
        _max.append(_arr[i][i])
    _fin.append(sum(_max))
    _max.clear()

    # 대각선
    for i in range(N):
        _max.append(_arr[i][N-i-1])
    _fin.append(sum(_max))
    _max.clear()
 
    print(f'#{test_case} {max(_fin)}')