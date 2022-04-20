# 틀렸음.....

import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
meetings = []
tmp = []
for _ in range(n):
    start, end = map(int, input().split())
    tmp.append((start, end))
    meetings.append((end-start, start, end))

tmp.sort()
start_hour = tmp[0][0]
end_hour = tmp[-1][1]
time_table = [0] * (end_hour - start_hour + 1 + 1)

meetings.sort()
cnt = 0
for m in meetings:
    if 1 in time_table[m[1]:m[2]]:
        continue
    else:
        cnt += 1
        time_table[m[1]:m[2]] = [1] * (m[2] - m[1])

print(cnt)