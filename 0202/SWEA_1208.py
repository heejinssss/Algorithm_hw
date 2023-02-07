N = int(input())
arr = list(map(int, input().split()))

cnt = 0
while cnt < N:
    _min = min(arr)
    _max = max(arr)
    if abs(_min - _max) <= 1:
        break
    arr[arr.index(_min)] = _min + 1
    arr[arr.index(_max)] = _max - 1
    cnt += 1

print(max(arr)-min(arr))