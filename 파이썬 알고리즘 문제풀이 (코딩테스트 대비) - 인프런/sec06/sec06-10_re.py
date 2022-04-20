# (성공!)
# 풀이시간: 9분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level, start_n):
    global cnt
    if level == m:
        for x in result:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(start_n, n+1):
            result[level] = i
            DFS(level+1, i+1)


n, m = map(int, input().split())
result = [0] * m
cnt = 0
DFS(0, 1)
print(cnt)