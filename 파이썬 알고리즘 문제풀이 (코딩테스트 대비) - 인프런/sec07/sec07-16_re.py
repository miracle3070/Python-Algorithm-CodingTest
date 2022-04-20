# 성공!
# 풀이시간: 8분

import sys
#sys.stdin = open("input.txt", "r")
# 좌, 우
dx = (-1, 1)

def DFS(y, x):
    visited[y][x] = 1
    if y == 0:
        print(x)
        return
    else:
        if 0 <= x-1 < 10 and table[y][x-1] == 1 and visited[y][x-1] == 0:
            DFS(y, x-1)
        elif 0 <= x+1 < 10 and table[y][x+1] == 1 and visited[y][x+1] == 0:
            DFS(y, x+1)
        else:
            DFS(y-1, x)


table = []
for _ in range(10):
    row = list(map(int, input().split()))
    table.append(row)
visited = [[0] * 10 for _ in range(10)]

start = -1
for i in range(10):
    if table[9][i] == 2:
        start = i
        break

DFS(9, start)


