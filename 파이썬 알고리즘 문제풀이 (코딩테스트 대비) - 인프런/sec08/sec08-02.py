# 성공!
# 풀이시간: 7분

import sys
#sys.stdin = open("input.txt", "r")


def calc(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if memory[n] == 0:
            result = calc(n-1) + calc(n-2)
            memory[n] = result
            return result
        else:
            return memory[n]


n = int(input())
memory = [0] * (n+1)
memory[1] = 1
memory[2] = 2
result = calc(n)
print(result)