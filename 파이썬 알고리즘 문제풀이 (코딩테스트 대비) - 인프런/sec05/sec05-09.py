# 풀이시간: 4분
import sys
#sys.stdin = open("input.txt", "r")


dict1 = dict()
dict2 = dict()
word1 = input()
word2 = input()

for w in word1:
    if w in dict1:
        dict1[w] += 1
    else:
        dict1[w] = 0

for w in word2:
    if w in dict2:
        dict2[w] += 1
    else:
        dict2[w] = 0

if dict1 == dict2:
    print("YES")
else:
    print("NO")