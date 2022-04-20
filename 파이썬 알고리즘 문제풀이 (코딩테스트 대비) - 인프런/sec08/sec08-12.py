# 성공하긴 했으나 왜 이렇게 풀어야되는지 이해가 안됨.

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


n, m = map(int,input().split())
table = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    table[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a][b] = c

# 처음에는 루프 변수를 a->b->k 순으로 적었으나 실패했음.
# 왜 k를 맨 먼저 적어야 하는가?
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            table[a][b] = min(table[a][b], table[a][k] + table[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if table[a][b] != INF:
            print(table[a][b], end=" ")
        else:
            print("M", end=" ")
    print()