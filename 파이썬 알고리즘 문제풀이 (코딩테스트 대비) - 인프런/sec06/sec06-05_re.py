# 풀이시간: 17분 (일부 케이스 타임아웃)
import sys
#sys.stdin = open("input.txt", "r")


def DFS(idx, sum):
    global result
    if sum > c:
        return
    if idx == n:
        if result < sum:
            result = sum
    else:
        if result < sum:
            result = sum
        DFS(idx+1, sum + weights[idx])
        DFS(idx+1, sum)



c, n = map(int, input().split())
weights = []
for _ in range(n):
    weights.append(int(input()))
result = -1
DFS(0, 0)
print(result)