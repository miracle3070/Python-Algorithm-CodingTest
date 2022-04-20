# 테스트케이스 1개 실패!
# 풀이시간: 20분

import sys
#sys.stdin = open('input.txt', "r")

# 좌, 우
dx = (-1, 1)


def DFS(y, x):
    t = False
    if y == 9:
        if table[y][x] == 2:
            return True
        else:
            return False
    else:
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < 10 and table[y][nx] == 1 and visited[y][nx] == 0:
                visited[y][nx] = 1
                t = DFS(y, nx)
                visited[y][nx] = 0
                break
        else:
            visited[y+1][x] = 1
            t = DFS(y+1, x)
            visited[y+1][x] = 0
    return t



table = []
for _ in range(10):
    row = list(map(int, input().split()))
    table.append(row)

visited = [[0] * 10 for _ in range(10)]


flag = False
result = -1

for i in range(10):
    flag = DFS(0, i)
    if flag:
        result = i
        break

print(result)