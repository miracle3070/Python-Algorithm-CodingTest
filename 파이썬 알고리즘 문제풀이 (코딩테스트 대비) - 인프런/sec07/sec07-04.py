# 일부 성공 (시간초과...)
# 풀이시간: 23분..
import sys
sys.stdin = open("input.txt", "r")


def DFS(total):
    global result
    if total > t:
        return
    if total == t:
        result.add(tuple(cnt))
        return
    else:
        for i in range(k):
            if cnt[i] > 0:
                cnt[i] -= 1
                DFS(total+coins[i])
                cnt[i] += 1


t = int(input())
k = int(input())
coins = []
cnt = []
result = set()
check = [0] * k
for _ in range(k):
    a, b = map(int, input().split())
    coins.append(a)
    cnt.append(b)

total = 0
for i in range(k):
    tmp = coins[i] * cnt[i]
    total += tmp


DFS(0)
print(len(result))

