# 성공!
# 풀이시간: 12분

import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

memory =[[0] * n for _ in range(n)]

# 초기화
memory[0][0] = board[0][0]
for i in range(1, n):
    memory[0][i] = memory[0][i-1] + board[0][i]
    memory[i][0] = memory[i-1][0] + board[i][0]

for y in range(1, n):
    for x in range(1, n):
        min_value = min(memory[y][x-1], memory[y-1][x])
        memory[y][x] = min_value + board[y][x]

print(memory[n-1][n-1])