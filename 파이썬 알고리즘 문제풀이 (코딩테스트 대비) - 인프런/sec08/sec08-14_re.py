# 성공!
# 풀이시간: 9분

from collections import deque
import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    target = q.popleft()
    print(target, end=" ")
    for x in graph[target]:
        degree[x] -= 1
        if degree[x] == 0:
            q.append(x)

