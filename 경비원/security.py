import sys
sys.stdin = open("input.txt", "r")

hor, ver = map(int, input().split()) # 10, 5
N = int(input())

security = []
for _ in range(N):
    temp = list(map(int, input().split()))
    security.append(temp)

donggeun = list(map(int, input().split()))

# [[1, 4], [3, 2], [2, 8]]
# [2, 3]
'''
10 5
3
1 4
3 2
2 8
2 3
'''
sum = 0
for item in security:
    temp = [item[0], donggeun[0]]
    if temp == [1, 2] or temp == [2, 1]:
        min_1 = ver + item[1] + donggeun[1]
        min_2 = 2*hor + ver - item[1] - donggeun[1]
        min_ = min(min_1, min_2)
    elif temp == [1, 3] or temp == [3, 1]:
        min_ = item[1] + donggeun[1]
    elif temp == [1, 4] or temp == [4, 1]:
        min_ = hor - item[1] + donggeun[1]
    elif temp == [2, 3] or temp == [3, 2]:
        min_ = ver - item[1] + donggeun[1]
    elif temp == [2, 4] or temp == [4, 2]:
        min_ = ver + hor - item[1] - donggeun[1]
    elif temp == [3, 4] or temp == [4, 3]:
        min_1 = hor + item[1] + donggeun[1]
        min_2 = 2*ver + hor - item[1] - donggeun[1]
        min_ = min(min_1, min_2)
    elif temp == [1, 1] or temp == [2, 2] or temp == [3, 3] or temp == [4, 4]:
        min_ = abs(item[1] - donggeun[1])
    
    print(min_)
    sum += min_
print(sum)