T = int(input())

for test_case in range(1, T + 1):

    try:
        *result, end = map(str, input().split())
        stack = []

        for num in result:
            if num.isdecimal(): # 피연산자이면
                stack.append(int(num))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if num == '-':
                    stack.append(b-a)
                elif num == '+':
                    stack.append(b+a)
                elif num == '*':
                    stack.append(b*a)
                elif num == '/':
                    stack.append(int(b/a))
        print(f'#{test_case}', end=' ')
        if not len(stack) == 1:
            print('error')
        else:
            print(*stack)
    except:
        print(f'#{test_case} error')