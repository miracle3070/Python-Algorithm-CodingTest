# 성공!
# 풀이시간: 10분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level, start_n):
    global cnt
    if level == k:
        total = sum(combination)
        if total % m == 0:
            cnt += 1
    else:
        for i in range(start_n, n):
            combination[level] = nums[i]
            DFS(level+1, i+1)


n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())

combination = [0] * k
cnt = 0
DFS(0, 0)
print(cnt)