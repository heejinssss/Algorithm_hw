import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    arr = []

    arr = [list(map(int, input().split())) for _ in range(100)]

# 2가 몇 열에 있는지 찾기
    x = 100-1
    y = arr[-1].index(2)

    while x != 0:
        if y+1 < 100 and arr[x][y+1] == 1: # 우
            arr[x][y] = 0
            y += 1
        elif y-1 > 0 and arr[x][y-1] == 1: # 좌
            arr[x][y] = 0
            y -= 1
        elif x-1 > 0: # 상
            x -= 1
        else:
            print(f'#{tc} {y}')
            break