'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3

A B C D E F
2 3 1 6 5 4
0         0
  0   0
    0   0
'''

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
pivot = dice.pop(0) # [2, 3, 1, 6, 5, 4]

for num in pivot:
    temp = [pivot.index(num)]
    for nums in dice:
        if num in nums:
            idx = nums.index(num) # 다음 주사위의 밑면 시작
            if idx == 0:
                idx = 5 # 그 주사위 윗면 인덱스
            elif idx == 1:
                idx = 3
            elif idx == 2:
                idx = 4
            elif idx == 3:
                idx = 1
            elif idx == 4:
                idx = 2
            elif idx == 5:
                idx = 0
            temp.append(idx) # 각 주사위들의 윗면 인덱스만 모아모아
    print(temp) # 꼭 삭제
    
    cnt = 0
    for i in temp:
        cmp = [i]
        if i == 0:
            i = 5
        elif i == 1:
            i = 3
        elif i == 2:
            i = 4
        elif i == 3:
            i = 1
        elif i == 4:
            i = 2
        elif i == 5:
            i = 0
        cmp.append(i)
        print(cmp) # 꼭 삭제
        dice.pop
        dice[cnt].remove(dice[max(cmp)])
        dice[cnt].remove(dice[min(cmp)])
        cnt += 1
    
    print(dice)


'''
[0, 4, 0, 1, 2]
[1, 5, 2, 3, 0]
[2, 3, 1, 5, 3]
[3, 2, 3, 4, 4]
[4, 0, 5, 0, 1]
[5, 1, 4, 2, 5]
'''