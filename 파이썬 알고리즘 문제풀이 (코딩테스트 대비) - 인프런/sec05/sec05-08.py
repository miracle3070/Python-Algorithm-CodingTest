# 풀이시간: 4분
import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
words = [input() for _ in range(n)]

for _ in range(n-1):
    word = input()
    words.remove(word)

print(words[0])