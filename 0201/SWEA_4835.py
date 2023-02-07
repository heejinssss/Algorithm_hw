N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 리스트에 구간합 저장
new_arr = []
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += arr[j+i]
        new = new_arr.append(sum)

# bubble sort
    for i in range(N-M, -1, -1):
        for j in range(i):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]

print(f'{new_arr[N-M]-new_arr[0]}')