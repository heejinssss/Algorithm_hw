T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    _list = list(map(int, input()))
    ans = cnt = 0
    for i in range(N):
        if _list[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt

    print(f'#{test_case} {ans}')