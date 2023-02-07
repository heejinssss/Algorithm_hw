T = int(input())
for test_case in range(1, T+1):

    ## 본인 풀이

    N = int(input())
    # N번 반복하면서 노선 입력, 빈도수 표시
    cnts = [0] * 5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1

    P = int(input())
    a_list = []
    # P번 반복하면서 정류장 번호 입력
    for _ in range(P):
        p = int(input())
        a_list.append(cnts[p])

    print(f'#{test_case}', *a_list)

    ## 교수님 풀이

    N = int(input())  # 버스 노선 개수
    lst1 = [list(map(int, input().split())) for _ in range(N)]  # 버스가 어디서부터 어디까지

    p = int(input())  # p개의 정류장
    lst2 = [int(input() for _ in range(p))]

    print(f'#{test_case}, end =''')

    # 정류장 검사
    for i in lst2:
        res = 0
        # 노선 범위 내에 있으면 += 1
        for j in lst1:
            if j[0] <= i <= j[1]:
                res += 1
            print(res, end=' ')
        print()