T = int(input())

for test_case in range(1, T + 1):
	
    N = int(input())
    arr = list(map(int, input().split()))

    n = 0

    while n < len(arr):

        for i in range(N-1, 0, -1):
            for j in range(n, i):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        n += 1

        for i in range(N-1, 0, -1):
            for j in range(n, i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        n += 1

    print(f'#{test_case}', end=' ')
    print(*arr[:10])