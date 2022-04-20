# 풀이시간: 8분
import sys
#sys.stdin = open("input.txt", "r")

exp = input()
stack = []
operand1 = -1
operand2 = -1
for e in exp:
    if e.isdigit():
        stack.append(int(e))
        continue
    operand2 = stack.pop()
    operand1 = stack.pop()
    if e == "+":
        result = operand1 + operand2
    elif e == "-":
        result = operand1 - operand2
    elif e == "*":
        result = operand1 * operand2
    else:
        result = operand1 // operand2
    stack.append(result)

result = stack.pop()
print(result)
