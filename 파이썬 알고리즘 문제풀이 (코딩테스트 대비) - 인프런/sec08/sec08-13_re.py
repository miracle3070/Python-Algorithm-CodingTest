# 성공!
# 풀이시간: 13분

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)

n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

min_value = INF

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        max_v = max(graph[a][1:])
        if max_v < min_value:
            min_value = max_v

result = []
for i in range(1, n+1):
    max_v = max(graph[i][1:])
    if max_v == min_value:
        result.append(i)


print(min_value, len(result))
for x in result:
    print(x, end=" ")
