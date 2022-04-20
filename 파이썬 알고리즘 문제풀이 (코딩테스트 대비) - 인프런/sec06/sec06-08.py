# 풀이시간: 12분 (성공!)
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level, nums):
    global cnt
    if level == m:
        for x in result:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(len(nums)):
            result[level] = nums[i]
            tmp = list(nums)
            tmp.remove(nums[i])
            DFS(level+1, tmp)


n, m = map(int, input().split())
cnt = 0
result = [0] * m
nums = list(range(1, n+1))
DFS(0, nums)
print(cnt)