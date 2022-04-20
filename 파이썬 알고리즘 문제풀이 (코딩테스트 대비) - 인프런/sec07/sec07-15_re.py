# 성공! (거의 실패했으나 테스트케이스를 보고 수정)
# 풀이시간: 25분
from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def check():
    cnt = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                cnt += 1
    return cnt


def BFS():
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))


m, n = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
result = 0
cnt = check()

q = deque()
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
           q.append((y, x))

BFS()
result = -1
for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            result = -1
            break
        else:
            if result < board[y][x]:
                result = board[y][x]
    if result == -1:
        break

if result != -1:
    print(result-1)
else:
    print(-1)

