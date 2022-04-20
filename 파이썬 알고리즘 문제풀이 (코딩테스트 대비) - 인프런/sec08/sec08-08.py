# 성공!
# 풀이시간: 9분

import sys
#sys.stdin = open("input.txt", "r")


def DFS(y, x):
    if y == 0 or x == 0:
        return memory[y][x]
    else:
        if memory[y][x] == 0:
            min_value = min(DFS(y-1, x), DFS(y, x-1))
            memory[y][x] = min_value + board[y][x]
        return memory[y][x]


n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

memory = [[0] * n for _ in range(n)]
memory[0][0] = board[0][0]
for i in range(1, n):
    memory[0][i] = memory[0][i-1] + board[0][i]
    memory[i][0] = memory[i-1][0] + board[i][0]

DFS(n-1, n-1)
print(memory[n-1][n-1])