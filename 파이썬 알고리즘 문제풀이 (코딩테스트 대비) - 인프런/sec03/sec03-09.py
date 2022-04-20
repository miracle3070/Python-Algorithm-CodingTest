import sys
#sys.stdin = open("input.txt.", "r")


n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# 위쪽, 왼쪽, 아래쪽, 오른쪽
dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)

cnt = 0
for y in range(n):
    for x in range(n):
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                if table[y][x] <= table[ny][nx]:
                    break
            else:
                continue
        else:
            cnt += 1

print(cnt)