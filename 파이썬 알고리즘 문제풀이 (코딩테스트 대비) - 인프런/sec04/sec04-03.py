# 틀렸음. 반례가 존재

import sys
#sys.stdin = open("input.txt", "r")


def count(length):
    total = 0
    cnt = 0
    for i in range(n):
        total += movies[i]
        if total < length:
            continue
        elif total > length:
            cnt += 1
            total = movies[i]
        else:
            cnt += 1
            total = 0
    if total != 0:
        cnt += 1
    return cnt


n, m = map(int, input().split())
movies = list(map(int, input().split()))

start = 1
end = sum(movies)
result = -1

while start <= end:
    mid = (start + end) // 2
    cnt = count(mid)
    if cnt > m:
        start = mid + 1
    elif cnt < m:
        result = mid
        end = mid - 1
    else:
        result = mid
        end = mid - 1

print(result)