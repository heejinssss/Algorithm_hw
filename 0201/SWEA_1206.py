N = int(input()) # 건물 개수
arr = list(map(int, input().split())) # 건물 높이
cnt = 0 # 조망권 확보 건물 개수 선언

# 기준 양 옆 2개 건물
for i in range(2, N-2): # 2 ~ N-3
    lr = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]

# bubble sort
    for j in range(len(lr)-1, 0, -1):
        for k in range(j):
            if lr[k] > lr[k+1]:
                lr[k], lr[k+1] = lr[k+1], lr[k]

# 가장 큰 건물이 기준 건물보다 작다면 차이 저장
    if lr[-1] < arr[i]:
            cnt += arr[i]-lr[-1]

print(f'{cnt}')