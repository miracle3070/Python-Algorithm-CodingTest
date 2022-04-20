# 실패!
# 풀이시간: 28분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(idx, result):
    global cnt
    if idx > len(code):
        return
    if idx == len(code):
        print(result)
        cnt += 1
    elif code[idx] == '0':
        return
    else:
        tmp = result + alpha[int(code[idx])]
        DFS(idx+1, tmp)
        if idx+1 <= len(code):
            temp = int(code[idx:idx+2])
            if temp <= 26:
                tmp = result + alpha[temp]
                DFS(idx+2, tmp)




code = input()
zero = code.find('0')
if zero != -1:
    code = code[:zero]
code = 'x' + code
alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0
DFS(1, "")
print(cnt)