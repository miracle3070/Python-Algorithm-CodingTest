# 실패!
import sys
sys.stdin = open("input.txt", "r")


def DFS(n):
    if num < n:
        return
    table[n] = 1
    print(table)
    DFS(n+1)
    for i in range(1, n+1):
        if table[i] == 1:
            print(i, end=" ")
    print()

    table[n] = 0
    print(table)
    DFS(n+1)
    for i in range(1, n+1):
        if table[i] == 1:
            print(i, end=' ')
    print()


num = int(input())
table = [0] * (num+1)
DFS(1)