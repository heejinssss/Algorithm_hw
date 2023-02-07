T = int(input())
for test_case in range(1, T+1):

    ## 본인 풀이

    N = int(input())

    sorted_list = []

    for _ in range(N):
        _list = list(map(int, input().split()))

        if _list[0] == 1:
            for x in range(_list[1], _list[2]+1):
                sorted_list.append(x)

        elif _list[0] == 2:
            sorting_list = []
            for num in range(_list[1], _list[2] + 1):
                if _list[1] % 2 == 0:
                    if num % 2 == 0:
                        sorted_list.append(num)
                else:
                    if num % 2 == 1:
                        sorted_list.append(num)

        elif _list[0] == 3:
            sorting_list = []
            for num in range(_list[1], _list[2]+1):
                if _list[1] % 2 == 0:
                     if num % 4 == 0:
                        sorted_list.append(num)
                else:
                     if (num % 3 == 0) & (num % 10 != 0) == True:
                        sorted_list.append(num)

    counter = {}
    for num in sorted_list:
        try:
            counter[num] += 1
        except:
            counter[num] = 1

    if max(counter.values()) == 1:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {max(counter.values())}')

    ## 교수님 풀이

    N = int(input())
    bus_station = [0] * 1001
    
    lst = [list(map(int, input().split())) for _ in range()]
    
    for bus in lst:
        A = bus[1] # 출발
        B = bus[2] # 종점
    
        bus_station[A] += 1
        bus_station[B] += 1
    
        if bus[0] == 0:
            for i in range(A+1, B):
                bus_station[i] += 1
    
        elif bus[0] == 1:
            # A + 2 (출발 정류소는 이미 방문했기 때문)
            for i in range(A+2, B, 2):
                bus_station[i] += 1
    
        elif bus[0] == 2:
            if A % 2: # 홀수
                for i in range(A + 1, B):
                    if (i % 3) and not (i % 10):
                        bus_station[i] += 1
                else: # 짝수
                    if not (i % 4):
                        for i in range(A + 1, B):
                            bus_station[i] += 1
    
        res = max(bus_station)