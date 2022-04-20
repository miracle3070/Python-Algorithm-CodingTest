# 시간초과! (60점)
# 풀이시간: 12분
import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


def DFS(m, cnt):
    global result
    if m < 0:
        return
    elif m == 0:
        if cnt < result:
            result = cnt
    else:
        for i in range(n):
            if coins[i] == 1:
                DFS(m-coins[i], cnt+1)
            else:
                tmp = m // coins[i]
                if tmp != 0:
                    DFS(m-(tmp * coins[i]), cnt+tmp)
                else:
                    DFS(m - coins[i], cnt + 1)


n = int(input())
coins = list(map(int, input().split()))
m = int(input())
result = INF
DFS(m, 0)
print(result)