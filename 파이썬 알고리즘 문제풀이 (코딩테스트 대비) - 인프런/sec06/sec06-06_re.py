# 실패! (40점, 풀이시간: 20분)
import sys
#sys.stdin = open("input.txt", "r")


def DFS(i, c):
    global cnt
    if c > m:
        return
    elif c == m:
        print(i, end=" ")
        print()
        cnt += 1
    else:
        for j in range(i, n+1):
            for k in range(1, n+1):
                print(j, end=" ")
                DFS(k, c+1)


cnt = 0
n, m = map(int, input().split())
DFS(1, 1)
print(cnt)