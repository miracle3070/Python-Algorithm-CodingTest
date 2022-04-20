# 성공!
# 풀이시간: 24분
import sys
#sys.stdin = open("input.txt", "r")


def calc_distance(pizza):
    dist = 0
    for h in house:
        tmp = int(1e9)
        for p in pizza:
            d = abs(h[0]-p[0]) + abs(h[1]-p[1])
            if d < tmp:
                tmp = d
        dist += tmp
    return dist


def DFS(level, start):
    global result
    if level == m:
        tmp = calc_distance(select)
        if tmp < result:
            result = tmp
    else:
        for i in range(start, len(pizza)):
            select[level] = pizza[i]
            DFS(level+1, i+1)





n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
result = int(1e9)

house = []
pizza = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            house.append((y, x))
        elif board[y][x] == 2:
            pizza.append((y, x))
        else:
            pass
select = [0] * m
check = [0] * len(pizza)

DFS(0, 0)
print(result)


