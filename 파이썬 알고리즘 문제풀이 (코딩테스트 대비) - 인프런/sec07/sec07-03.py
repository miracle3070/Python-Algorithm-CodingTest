# 성공! (집합 연산으로 해결)
# 풀이시간: 22분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(level):
    if level == k:
        tmp = [weight[i] for i in range(k) if check[i] == 1]
        result.append(tmp)
    else:
        check[level] = 1
        DFS(level+1)
        check[level] = 0
        DFS(level+1)




k = int(input())
weight = list(map(int, input().split()))
total = sum(weight)
entire = set(range(1, total))
result = []
check = [0] * k

DFS(0)

result2 = []
for i in result:
    for k in result:
        tmp = sum(i) - sum(k)
        if tmp > 0:
            result2.append(tmp)

result2 = set(result2)
cnt = len(entire - result2)
print(cnt)
