import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

max_value = 0

# 각 행의 합 계산
for i in range(n):
    total = sum(table[i])
    if max_value < total:
        max_value = total

# 각 열의 합 계산
for i in range(n):
    total = 0
    for k in range(n):
        total += table[k][i]
    if max_value < total:
        max_value = total

# 대각선1의 합 계산
total = 0
for i in range(n):
    total += table[i][i]
if max_value < total:
    max_value = total

# 대각선 2의 합 계산
total = 0
for i in range(n):
    total += table[i][n-1-i]
if max_value < total:
    max_value = total

print(max_value)