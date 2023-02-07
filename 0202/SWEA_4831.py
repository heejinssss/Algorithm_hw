K, N, M = map(int, input().split())
charge = list(map(int, input().split()))
print(charge)

cnt = 0 # 들른 충전기 정류장 수
cur = 0 # 현위치


while cur + K < N:                  # 현재 위치한 곳에서 최대로 이동하지 않아도 목적지에 도착한다면 루프문 스탑
    for go in range(K, 0, -1):
        if cur + go in charge:      # 현재 위치 + 이동한 거리 == 마침 충전소 위치이면
            cur += go               # 현재 위치 갱신
            cnt += 1                # 충전소 들렀으니 count + 1
            break                   # while문 다시 시작하러

    else:
        cnt = 0
        break

print(cnt)