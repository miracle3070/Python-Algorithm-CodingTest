# 미해결
# 풀이시간: 32분

import sys
sys.stdin = open("input.txt", "r")


exp = input()
stack = []

for e in exp:
    if e.isdigit():
        print(e, end="")
        continue
    else:
        if not stack:
            stack.append(e)
            continue
        if e == "+" or e == "-":
            if stack[-1] != '(':
                target = stack.pop()
                print(target, end="")
            stack.append(e)
        elif e == "*" or e == "/":
            if stack[-1] == "+" or stack[-1] == "-":
                stack.append(e)
            else:
                if stack[-1] != '(':
                    target = stack.pop()
                    print(target, end="")
                stack.append(e)
        elif e == '(':
            stack.append(e)
        else:
            target = stack.pop()
            while target != '(':
                print(target, end="")
                target = stack.pop()

while stack:
    target = stack.pop()
    print(target, end="")
