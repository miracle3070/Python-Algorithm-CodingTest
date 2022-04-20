# 성공!
# 문제를 잘못 이해해서 한참을 해맴...
# 풀이시간: 25분

import sys
#sys.stdin = open("input.txt", "r")
# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def DFS(x, y):
    global cnt
    if x == rx and y == ry:
        cnt += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and table[y][x] < table[ny][nx]:
                visited[ny][nx] = 1
                DFS(nx, ny)
                visited[ny][nx] = 0


n = int(input())
table = []
rx = ry = 0
sx = sy = 0
max_value = 0
min_value = int(1e9)
for i in range(n):
    row = list(map(int, input().split()))
    table.append(row)
    for k in range(n):
        if max_value < row[k]:
            max_value = row[k]
            rx = k
            ry = i
        if min_value > row[k]:
            min_value = row[k]
            sx = k
            sy = i


visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

cnt = 0
DFS(sx, sy)
print(cnt)
