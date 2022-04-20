# 성공!
# 풀이시간: 21분

import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)


n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n):
    graph[i][i] = 0

n1, n2 = 1,1
while n1 != -1 and n2 != -1:
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])



min_value = INF
for i in range(1, n+1):
    max_v = 0
    for k in range(1, n+1):
       if graph[i][k] != INF and graph[i][k] > max_v:
           max_v = graph[i][k]
    if max_v < min_value:
        min_value = max_v

elect = []
cnt = 0
for i in range(1, n+1):
    max_v = 0
    for k in range(1, n+1):
       if graph[i][k] != INF and graph[i][k] > max_v:
           max_v = graph[i][k]
    if max_v == min_value:
        cnt += 1
        elect.append(i)

print(min_value, cnt)
for x in elect:
    print(x, end=" ")

for x in graph:
    print(x)