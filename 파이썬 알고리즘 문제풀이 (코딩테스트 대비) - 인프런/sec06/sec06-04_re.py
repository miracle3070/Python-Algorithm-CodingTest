# 풀이시간: 22분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(idx):
    if idx >= len(origin):
        tmp = []
        for i in range(len(table)):
            if table[i] == 1:
                tmp.append(i)
        result.append(set(tmp))
    else:
        table[origin[idx]] = 1
        DFS(idx+1)
        table[origin[idx]] = 0
        DFS(idx+1)



n = int(input())
origin = list(map(int, input().split()))
table = [0] * (max(origin) + 1)
result = []

DFS(0)
for i in range(len(result)):
    target = result[i]
    oppo = set(origin) - target
    if sum(target) == sum(oppo):
        print("YES")
        break
else:
    print("NO")