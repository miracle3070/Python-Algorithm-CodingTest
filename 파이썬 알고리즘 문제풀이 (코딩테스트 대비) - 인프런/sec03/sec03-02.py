# 4분만에 해결
#import sys
#sys.stdin = open("input.txt", "r")


string = input()
num = ""
for s in string:
    if s.isdigit():
        num += s

# 최종 자연수
num = int(num)

# 약수 구하기
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1

# 결과 출력
print(num)
print(count)