# 성공!
# 풀이시간 11분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")

# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


table = []
for _ in range(7):
    row = list(map(int, input().split()))
    table.append(row)

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx <= 6 and 0 <= ty <= 6:
            if table[ty][tx] == 0:
                table[ty][tx] = table[y][x] + 1
                q.append((tx, ty))

if table[6][6] != 0:
    print(table[6][6])
else:
    print(-1)