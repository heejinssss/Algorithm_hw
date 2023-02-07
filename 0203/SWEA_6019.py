"""
1
250 10 15 20
"""

T = int(input())
for test_case in range(1, T+1):

    D, A, B, F = map(int, input().split())

    # mile = 0.0
    # x = 0.0
    #
    # while D > 0:
    #     x = (F*D)/(B+F) # 파리의 이동 거리
    #     mile += x
    #     D -= (x/F)*25
    #     if D < 0:
    #         break
    #     x = (F*D)/(A+F) # 파리의 이동 거리
    #     mile += x
    #     D -= (x/F)*25
    #
    # print(f'#{test_case} {round(mile)}')