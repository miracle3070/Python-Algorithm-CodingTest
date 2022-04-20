# 시간 초과
import sys
#sys.stdin = open("input.txt", "r")


k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

max_line = max(lines)
result = -1
for c in range(max_line, 0, -1):
    cnt = 0
    for line in lines:
        cnt += line // c
    if cnt >= n:
        result = c
        break

print(result)