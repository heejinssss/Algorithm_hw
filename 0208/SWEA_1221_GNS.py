T = int(input())

for test_case in range(1, T + 1):

    sharp, N = map(str, input().split())
    new_nums = list(map(str, input().split()))
    nums_table = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    ans = []

    i = 0
    for nums in new_nums:
        new_nums[i] = nums_table[nums]
        i += 1

    for i in range(10):
        cnt = new_nums.count(i) # 숫자별 개수 세기
        ans += [list(nums_table.keys())[i] for _ in range(cnt)]

    print(sharp)
    print(*ans)