arr = [list(map(int, input().split())) for _ in range(100)]

x = 0
y = 0

# 2가 몇 열에 있는지 찾기
for j in range(100):
    if arr[99][j] == 2:
        x, y = 99, j

di = [-1, 0, 1] # 좌 우 상
dj = [0, -1, 0]

while y > 0:
    for k in range(3):
        x += di[k]
        y += dj[k]
        print(1)
        if (0 <= x < 99) & (0 <= y < 99) & (arr[x][y] == 1):
            print(2)
        break
print(3)
print(x)