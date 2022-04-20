# 성공!
# 풀이시간: 20분
from collections import deque
import sys, copy
#sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def BFS(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] > 0:
                    board[ny][nx] = 0
                    q.append((ny, nx))


n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

result = []
origin = copy.deepcopy(board)
cnt = 0

for h in range(1, 101):
    for y in range(n):
        for x in range(n):
            if 0 < board[y][x] <= h:
                board[y][x] = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                cnt += 1
                BFS(y, x)
    result.append(cnt)
    cnt = 0
    board = copy.deepcopy(origin)

result_v = max(result)
print(result_v)