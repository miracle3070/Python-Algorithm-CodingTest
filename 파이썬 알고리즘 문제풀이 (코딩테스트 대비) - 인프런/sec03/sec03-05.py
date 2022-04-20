# 시간 초과 판정
import sys
#sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(len(nums)):
    total = 0
    for k in range(i, len(nums)):
        total += nums[k]
        if total == m:
            cnt += 1
            break
        elif total > m:
            break
        else:
            continue

print(cnt)
