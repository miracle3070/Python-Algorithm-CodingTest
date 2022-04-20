import sys

#sys.stdin = open("input.txt", "r")

table = [list(map(int, input().split())) for _ in range(9)]
flag = True

# 각 행을 검사
for r in range(9):
    cnt = len(set(table[r]))
    if cnt != 9:
        flag = False
        break

# 각 컬럼을 검사
if flag:
    for c in range(9):
        tmp = []
        for r in range(9):
            tmp.append(table[r][c])
        cnt = len(set(tmp))
        if cnt != 9:
            flag = False
            break
# 각 칸을 검사
if flag:
    tmp = []
    x = y = 0
    while x < 9:
        tmp += table[y][x:(x+3)]
        y += 1
        if y % 3 == 0:
            cnt = len(set(tmp))
            if cnt != 9:
                flag = False
                break
        if y >= 9:
            y = 0
            x += 3

if flag:
    print("YES")
else:
    print("NO")
