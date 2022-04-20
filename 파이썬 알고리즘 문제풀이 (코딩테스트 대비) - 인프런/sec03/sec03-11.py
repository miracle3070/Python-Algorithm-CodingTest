import sys

#sys.stdin = open("input.txt", "r")


def is_true(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


table = ["".join(input().split()) for _ in range(7)]
cnt = 0


# 행 기준으로 카운트
for i in range(7):
    for k in range(3):
        target_row = table[i][k:(k+5)]
        if is_true(target_row):
            cnt += 1


# 열 기준으로 카운트
for i in range(7):
    for k in range(3):
        target = ""
        for a in range(5):
            target += table[k + a][i]
        if is_true(target):
            cnt += 1


print(cnt)

