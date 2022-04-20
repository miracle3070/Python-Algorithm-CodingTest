# 성공!
# 풀이시간: 11분
import sys
#sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if 0 <= rx <= 6 and 0<= ry <= 6 and board[ry][rx] == 0:
                if visited[ry][rx] == 0:
                    visited[ry][rx] = 1
                    DFS(rx, ry)
                    visited[ry][rx] = 0




board = []
for _ in range(7):
    row = list(map(int, input().split()))
    board.append(row)
visited = [[0] * 7 for _ in range(7)]
cnt = 0
visited[0][0] = 1
DFS(0, 0)

print(cnt)