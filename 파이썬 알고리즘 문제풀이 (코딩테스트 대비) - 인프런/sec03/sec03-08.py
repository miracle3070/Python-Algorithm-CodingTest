from collections import deque
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

m = int(input())
for _ in range(m):
    # 행번호, 방향, 회전 수
    r, d, c = map(int, input().split())
    target = deque(table[r-1])
    if d == 0: # 왼쪽
        for _ in range(c):
            tmp = target.popleft()
            target.append(tmp)
    else: # 오른쪽
        for _ in range(c):
            tmp = target.pop()
            target.appendleft(tmp)
    table[r-1] = list(target)


mid = n // 2
start = 0
end = n - 1
total = 0
for i in range(n):
    for k in range(start, end+1):
        total += table[i][k]
    if i < mid:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(total)