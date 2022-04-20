#import sys
#sys.stdin = open("input.txt", "r")


def is_true(s):
    n = len(s)
    s = s.upper()
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


n = int(input())
for i in range(1, n + 1):
    string = input()
    if is_true(string):
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")
