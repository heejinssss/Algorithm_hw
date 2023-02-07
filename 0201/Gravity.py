N = int(input())
boxes = list(map(int, input().split()))
mx = 0
for (i, box) in enumerate(boxes):
    count = 0
    for right_box in boxes[i + 1:]:
        if box > right_box:
            count += 1
    if count > mx:
        mx = count
print(mx)