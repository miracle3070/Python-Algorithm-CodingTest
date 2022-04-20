# 성공!
# 풀이시간: 8분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


s, e = map(int, input().split())
table = [INF] * 10001
visited = [0] * 10001
table[s] = 0
queue = deque([s])
result = INF


while queue:
    cur = queue.popleft()
    if cur == e:
        result = table[e]
        break
    for dx in (1, -1, 5):
        t = cur + dx
        if 1 <= t <= 10000:
            if visited[t] == 0:
                visited[t] = 1
                table[t] = table[cur] + 1
                queue.append(t)

print(result)