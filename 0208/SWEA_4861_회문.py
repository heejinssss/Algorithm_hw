T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split()) # N by M 배열
    arr = []

    for _ in range(N):
        a = list(map(str, input().split()))
        arr.append(a[0])

    # 행 기준으로 찾기
    for i in range(N):
        for k in range(N-M+1):
            if arr[i][k:M+k] == (arr[i][k:M+k])[::-1]:
                print(f'#{test_case}', end=' ')
                print(arr[i][k:M+k])
                break

    # 열 기준으로 찾기
    for j in range(N):
        cache = []
        for i in range(N):
            cache.append(arr[i][j])
        for k in range(N-M+1):
            if cache[k:M+k] == (cache[k:M+k])[::-1]:
                fin = cache[k:M+k]
                print(f'#{test_case}', end=' ')
                print(''.join(fin))