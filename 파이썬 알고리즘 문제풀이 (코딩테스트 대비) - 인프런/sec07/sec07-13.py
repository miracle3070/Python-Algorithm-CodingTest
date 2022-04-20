# 성공!
# 풀이시간: 11분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우, 왼위, 오위, 오아, 왼아
dx = (0, 0, -1, 1, -1, 1, 1, -1)
dy = (-1, 1, 0, 0, -1, -1, 1, 1)


def BFS(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 1:
                    board[ny][nx] = 2
                    q.append((ny, nx))


n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
cnt = 0

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            cnt += 1
            BFS(y, x)

print(cnt)

