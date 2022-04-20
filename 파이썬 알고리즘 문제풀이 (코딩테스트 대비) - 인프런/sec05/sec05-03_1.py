# 풀이시간: 32분
import sys
#sys.stdin = open("input.txt", "r")


exp = input()
level_1 = ['+', '-']
level_2 = ['*', '/']
stack = []

for e in exp:
    if e.isdigit():
        print(e, end="")
        continue
    elif not stack or e == '(':
        stack.append(e)
    elif e in level_1:
        if stack[-1] == '(':
            stack.append(e)
        else:
            while stack and (stack[-1] in level_2 or stack[-1] in level_1):
                oper = stack.pop()
                print(oper, end="")
            stack.append(e)
    elif e in level_2:
        if stack[-1] == '(' or stack[-1] in level_1:
            stack.append(e)
        else:
            while stack and (stack[-1] in level_2):
                oper = stack.pop()
                print(oper, end="")
            stack.append(e)
    elif e == ')':
        oper = stack.pop()
        while oper != '(':
            print(oper, end="")
            oper = stack.pop()
    else:
        pass

while stack:
    oper = stack.pop()
    print(oper, end="")
