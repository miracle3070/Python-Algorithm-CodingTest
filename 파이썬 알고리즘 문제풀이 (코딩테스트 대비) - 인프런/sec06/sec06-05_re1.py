# 풀이시간: 9분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(idx, sum, tsum):
    global result
    if sum + (total-tsum) < result:
        return
    if sum > c:
        return
    if idx == n:
        if sum > result:
            result = sum
    else:
        DFS(idx+1, sum+weights[idx], tsum+weights[idx])
        DFS(idx+1, sum, tsum+weights[idx])


c, n = map(int, input().split())
weights = [int(input()) for _ in range(n)]
result = 0
total = sum(weights)

DFS(0, 0, 0)
print(result)