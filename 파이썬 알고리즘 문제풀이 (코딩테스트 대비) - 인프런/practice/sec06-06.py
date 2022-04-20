# 성공!
# 풀이시간: 5분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level):
    global cnt
    if level == m:
        for x in result:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            result[level] = i
            DFS(level + 1)



n, m = map(int, input().split())
result = [0] * m
cnt = 0
DFS(0)
print(cnt)