import sys, copy
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(1, T+1):
    N = int(input())

    data = []
    for _ in range(N):
        num = list(input())
        data.append(num)   

    visited = [[0]*(N) for _ in range(N)]

    for i in range(N):
        if '2' in data[i]:
            x = data[i].index('2')
            y = i

    # while data[y][x] != '3':
    while True:
        if 0 <= y <= N-1 and 0 <= x-1 <= N-1 and (data[y][x-1] == '0' or data[y][x-1] == '3') and visited[y][x-1] == 0 :
            x -= 1
        elif 0 <= y-1 <= N-1 and 0 <= x <= N-1 and (data[y-1][x] == '0' or data[y-1][x] == '3') and visited[y-1][x] == 0:
            y -= 1
        elif 0 <= y <= N-1 and 0 <= x+1 <= N-1 and (data[y][x+1] == '0' or data[y][x+1] == '3') and visited[y][x+1] == 0:
            x += 1
        visited[y][x] = 1
        print(visited)
        
        # 3 찾았으면
        if data[y][x] == '3':
            print(1)
            break
        elif y == 0:
            print(0)
            break