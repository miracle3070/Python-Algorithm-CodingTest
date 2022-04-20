# 성공! (몇 번의 수정 끝에 성공함.. 강의 풀이와는 다름)
# 풀이시간: 17분
import sys
#sys.stdin = open("input.txt", "r")


def DFS(idx, result):
    global cnt
    if idx > len(code):
        return
    if idx == len(code):
        print(result)
        cnt += 1
        return
    else:
        if code[idx] == '0':
            return
        else:
            tmp = int(code[idx])
            DFS(idx+1, result+alpha[tmp])
            if idx+1 < len(code):
                tmp = int(code[idx:idx+2])
                if tmp <= 26:
                    DFS(idx+2, result+alpha[tmp])


code = input()
alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0
DFS(0, "")
print(cnt)


