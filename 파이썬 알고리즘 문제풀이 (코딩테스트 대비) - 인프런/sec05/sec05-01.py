# 실패 (20점)
# 풀이시간: 25분
import sys
#sys.stdin = open("input.txt", "r")


num, cnt = input().split()
num = list(num)
cnt = int(cnt)

stack = []
cur_cnt = 0
i = 0
while cur_cnt < cnt:
    if stack == [] or stack[-1] == num[i]:
        stack.append(num[i])
        i += 1
    elif stack[-1] < num[i]:
        while stack and stack[-1] < num[i]:
            target = stack.pop()
            num.remove(target)
            cur_cnt += 1
            if cur_cnt >= cnt:
                break
        stack.append(num[i])
        i += 1
    else:
        num.pop(i)
        cur_cnt += 1

print("".join(num))

