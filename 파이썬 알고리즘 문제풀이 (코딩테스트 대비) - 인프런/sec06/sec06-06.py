# 실패! (22분간 도전)
import sys
sys.stdin = open("input.txt", "r")


def DFS(i, k):
    if k > n:
        return
    if i > m:
        for i in range(1, m+1):
            print(nums[i], end=" ")
        print()
    else:
        nums[i] = k
        DFS(i+1, k)
        nums[i] = k+1
        DFS(i+1, k+1)





n, m = map(int, input().split())
nums = [0] * (m+1)
print(nums)
result = []
DFS(1, 1)