# 성공!
# 풀이시간: 12분

import sys
#sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
memory = [0] * (m+1)
w = []
v = []
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(n):
    weight = w[i]
    value = v[i]
    for k in range(weight, m+1):
        if memory[k] < memory[k-weight] + value:
            memory[k] = memory[k-weight] + value

print(memory[m])