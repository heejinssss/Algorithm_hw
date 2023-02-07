num = int(input())
C = [0] * 10 # 0 ~ 9

for i in range(6):
    C[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if C[i] >= 3: # tri
        C[i] -= 3
        tri += 1
        continue
    if C[i] >= 1 and C[i+1] >= 1 and C[i+2] >= 1: # run
        C[i] -= 1
        C[i+1] -= 1
        C[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print(1)
else:
    print(0)