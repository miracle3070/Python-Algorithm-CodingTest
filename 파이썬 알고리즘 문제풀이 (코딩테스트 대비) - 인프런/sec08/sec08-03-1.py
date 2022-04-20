# 성공!
# 2번 풀이방법과 중복

import sys
sys.stdin = open("input.txt", "r")


def DFS(n):
    if n == 1 or n == 2:
        return n
    elif memory[n] != 0:
        return memory[n]
    else:
        res = DFS(n-1) + DFS(n-2)
        memory[n] = res
        return res

n = int(input())
memory = [0] * (n+1)
DFS(n)
print(memory[n])