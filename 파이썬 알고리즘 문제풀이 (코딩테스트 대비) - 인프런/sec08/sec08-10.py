# 성공!
# 풀이시간: 9분

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


n = int(input())
coins = list(map(int, input().split()))
m = int(input())

memory = [INF] * (m+1)
memory[0] = 0

for i in range(n):
    coin = coins[i]
    for k in range(coin, m+1):
        if memory[k] > memory[k-coin] + 1:
            memory[k] = memory[k-coin] + 1

print(memory[m])