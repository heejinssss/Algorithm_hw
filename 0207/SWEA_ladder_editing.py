arr = [list(map(int, input().split())) for _ in range(100)]

x = 0
y = 0

# 2가 몇 열에 있는지 찾기
for j in range(100):
    if arr[99][j] == 2:
        x, y = 99, j # 57

di = [-1, 0, 1] # 좌 우 상
dj = [0, -1, 0]

cnt = 0
k = 0

while x > 0:
    print(x, y)
    if (0 <= x + di[k] < 99) & (0 <= y + dj[k] < 99) & (arr[x+di[k]][y+dj[k]] == 1):
        x += di[k]
        y += dj[k]
        k = 0
        cnt += 1
    else:
        k = (k + 1) % 3
print(cnt)