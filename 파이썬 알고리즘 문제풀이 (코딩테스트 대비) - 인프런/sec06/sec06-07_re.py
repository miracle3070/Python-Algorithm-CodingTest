# 풀이시간: 14분 (성공!)
import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


def DFS(level, total):
    global result
    if level > result:
        return
    if total > m:
        return
    elif total == m:
        if level < result:
            result = level
    else:
        for i in range(n):
            DFS(level+1, total + coins[i])


n = int(input()) # 동전의 종류 개수
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input()) # 거슬러줄 금액
result = INF
DFS(0, 0)

print(result)