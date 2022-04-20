# 실패
import sys
sys.stdin = open("input.txt", "r")


def dfs(i, s):
    if len(weights) <= i or c <= s:
        return 0
    total_o = weights[i] + dfs(i+1, s + weights[i])
    total_x = dfs(i+1, s)
    results.append(total_o)
    results.append(total_x)


c, n = map(int, input().split())
weights = [int(input()) for _ in range(n)]
results = []

dfs(0, 0)
result = max(results)
print(result)