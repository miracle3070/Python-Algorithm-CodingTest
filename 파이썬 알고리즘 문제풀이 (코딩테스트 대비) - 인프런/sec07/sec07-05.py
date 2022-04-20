# 성공!
# 풀이시간: 8분
import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


def DFS(level, a, b, c):
    global result
    if level == n:
        if a != b and b != c and c != a:
            tmp = [a, b, c]
            temp = max(tmp) - min(tmp)
            if temp < result:
                result = temp
    else:
        DFS(level+1, a + coins[level], b, c)
        DFS(level+1, a, b + coins[level], c)
        DFS(level+1, a, b, c + coins[level])


n = int(input()) # 동전의 개수
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

result = INF
DFS(0, 0, 0, 0)
print(result)