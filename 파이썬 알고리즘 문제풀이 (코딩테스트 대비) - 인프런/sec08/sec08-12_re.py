# 실수로 틀렸다가 해결함.
# 풀이시간: 8분

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 이 부분을 빼먹어서 틀림!!
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("M", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()