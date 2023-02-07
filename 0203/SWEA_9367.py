"""
3
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    ans = [1]

    for i in range(1, N): # 0 1 2 3 4
        if C[i-1] == C[i]-1:
            cnt += 1
            ans.append(cnt)
            print(ans)
        else:
            cnt = 1 # 연결되는 숫자가 한개도 없는 경우

    result = max(ans)
    print(f'#{test_case} {result}')