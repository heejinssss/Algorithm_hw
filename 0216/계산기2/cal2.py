import sys
sys.stdin = open("input.txt", "r")

T = 10
 
for test_case in range(1, T + 1):
 
    N = int(input())
    infix = input()
    stack = []
    result = ''
 
    # 변환할 식을 순회
    for token in infix:
        # (1) 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token
        # (2) 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stck에 push
            if not stack: # stack이 비었다면
                stack.append(token)
            else:
                # icp가 2인 경우
                if token == '*':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack에서 pop, result에 append
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(token)
 
                # icp가 1인 경우
                elif token == '+':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack에서 pop, result에 append
                    # '('가 아닌 경우 모두 동치
                        while stack and stack[-1] != '(':
                            result += stack.pop()
                        stack.append(token)
    while stack:
        result += stack.pop()
 
    stack = []
 
    for num in result:
        if num.isdecimal(): # 피연산자이면
            stack += num
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if num == '+':
                stack.append(b+a)
            elif num == '*':
                stack.append(b*a)
    
    print(f'#{test_case}', end=' ')
    print(*stack)