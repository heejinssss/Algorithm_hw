N = int(input())
A = list(map(int, input()))
B = []
C = [0] * (max(A)+1)

for i in range(0, len(A)):
    C[A[i]] += 1

_Ci = 0
_C = 0

for j in range(len(C)):
    if C[j] >= _C:
        _C = C[j]
        _Ci = j

print(f'{_Ci} {_C}')