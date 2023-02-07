'''
Q. 빨간색, 파란색 색종이가 겹쳐져서 만들어지는 보라색 영역의 칸 수를 구하기

1. 두 색종이가 차지하는 영역에 속하는 칸 인덱스를 각각 다른 리스트에 저장
2. 두 리스트에서 서로 겹치는 원소 개수 카운트
'''

T = int(input())
 
for test_case in range(1, T + 1):
  
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
  
    num_red = []
    num_blue = []
  
    for i in range(N):
        arr_ith = []
        arr_jth = []
        idx0 = arr[i][0]
        idx1 = arr[i][1]
  
        while idx0 <= arr[i][2]:
            arr_ith.append(idx0)
            idx0 += 1
  
        while idx1 <= arr[i][3]:
            arr_jth.append(idx1)
            idx1 += 1
  
        if arr[i][-1] == 1:
            for numi in arr_ith:
                for numj in arr_jth:
                    num_red.append([numi, numj])
  
        if arr[i][-1] == 2:
            for numi in arr_ith:
                for numj in arr_jth:
                    num_blue.append([numi, numj])
  
    cnt = 0
    if len(num_blue) >= len(num_red):
        for num in num_red:
            if num in num_blue:
                cnt += 1
    else:
        for num in num_blue:
            if num in num_red:
                cnt += 1
  
    print(f'#{test_case} {cnt}')