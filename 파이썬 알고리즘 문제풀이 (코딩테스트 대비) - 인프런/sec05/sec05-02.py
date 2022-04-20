# 풀이시간: 18분
import sys
#sys.stdin = open("input.txt", "r")


map_list = input()
stack = []
result = 0
prev = '('

for x in map_list:
    if x == '(':
        stack.append(x)
        prev = '('
    else:
        if prev == '(':
            stack.pop()
            result += len(stack)
            prev = ')'
        else:
            result += 1
            stack.pop()

print(result)

