# 실패!
# 풀이시간: 25분
import sys
sys.stdin = open("input.txt", "r")


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


def BFS(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                visited[ny][nx] = 1


m, n = map(int, input().split()) # 가로, 세로
board = []
result = 0
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)


cnt = check()
while cnt > 0:
    visited = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                BFS(y, x)
    result += 1
    temp = check()
    if cnt != temp:
        cnt = temp
    else:
        result = -1

print(result)
