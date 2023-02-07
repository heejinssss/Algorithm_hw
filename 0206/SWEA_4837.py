'''
Q. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수

비트 연산자를 이용하여, 부분집합의 개수 구하기
'''

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    new_arr = []

    for i in range(1 << 12):  # 1<<N : 부분집합의 원소 개수
        i_arr = []
        for j in range(12):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                i_arr.append(arr[j])
        new_arr.append(i_arr)

    cnt = 0
    for nums in new_arr:
        if (sum(nums) == K) & (len(nums) == N) == True:
            cnt += 1
    print(f'#{test_case} {cnt}')