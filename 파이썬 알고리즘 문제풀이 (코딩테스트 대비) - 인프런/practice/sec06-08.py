# 성공!
# 깜빡하고 시간 못잼 ㅠㅠ
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
            if check[i] != 1:
                check[i] = 1
                result[level] = i
                DFS(level+1)
                check[i] = 0



n, m = map(int, input().split())
result = [0] * m
check = [0] * (n+1)
cnt = 0
DFS(0)
print(cnt)