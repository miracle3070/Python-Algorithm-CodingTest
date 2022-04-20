# 성공!
# 풀이시간: 18분
# 이 문제 역시 문제를 제대로 안읽어서 오래걸림. (오름차순 하는 거 ㅠㅠ)
import sys
#sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def DFS(y, x):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and table[ny][nx] == '1':
            table[ny][nx] = '0'
            cnt += 1
            DFS(ny, nx)





n = int(input())
table = []
for _ in range(n):
    row = list(input())
    table.append(row)

result = []
for y in range(n):
    for x in range(n):
        if table[y][x] == '1':
            cnt = 1
            table[y][x] = '0'
            DFS(y, x)
            result.append(cnt)

result.sort()
print(len(result))
for r in result:
    print(r)