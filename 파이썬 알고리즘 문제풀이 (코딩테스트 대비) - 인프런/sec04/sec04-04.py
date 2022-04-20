# 풀이시간: 26분 46초

import sys
#sys.stdin = open("input.txt", "r")


def count(mid):
    cnt = 1
    total = 0
    for i in range(len(dist)):
        if dist[i] < mid:
            total += dist[i]
            if total >= mid:
                cnt += 1
                total = 0
        else:
            cnt += 1
            total = 0
    return cnt


n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()
dist = [pos[i+1] - pos[i] for i in range(n-1)]


start = 1
end = max(pos) - min(pos)
result = -1

while start <= end:
    mid = (start + end) // 2
    cnt = count(mid)
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)