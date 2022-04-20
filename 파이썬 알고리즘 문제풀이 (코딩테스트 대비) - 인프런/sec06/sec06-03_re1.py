# 풀이시간: 7분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(num):
    if n < num:
        for i in range(1, n+1):
            if table[i] == 1:
                print(i, end=" ")
        print()
    else:
        table[num] = 1
        DFS(num+1)
        table[num] = 0
        DFS(num+1)




n = int(input())
table = [0] * (n+1)
DFS(1)