N = int(input())

plus_minus = 0

# 입력값이 음수이면
if N < 0:
    N = -N
    plus_minus += 1

new_copy = 0
new_copy += N

# str으로 변환된 값 담을 변수
ans = ''

# int값 자릿수
cnt = 0
while N > 0:
   N //= 10
   cnt += 1

N += new_copy

while cnt > 0:
    mul = 10**(cnt-1)
    num = N // mul
    ans += chr(ord('0') + num)
    N -= num*mul
    cnt -= 1
    num = 0

if plus_minus == 1:
    ans = '-' + ans
print(ans, type(ans))