# 풀이시간: 6분
import sys
#sys.stdin = open("input.txt", "r")


def binary(n):
    if n > 0:
        q = n // 2
        r = n % 2
        return str(r) + binary(q)
    else:
        return ""


num = int(input())
result = binary(num)
print(result[::-1])