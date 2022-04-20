# 풀이시간: 12분
import sys
sys.stdin = open("input.txt", "r")


# 전위순회
def pre_search(tree, n):
    print(n, end=" ")
    if n >= len(tree):
        return
    pre_search(tree, tree[n][0])
    pre_search(tree, tree[n][1])


# 중위순회
def in_search(tree, n):
    if n >= len(tree):
        print(n, end=" ")
        return
    in_search(tree, tree[n][0])
    print(n, end=" ")
    in_search(tree, tree[n][1])


# 후위순회
def post_search(tree, n):
    if n >= len(tree):
        print(n, end=" ")
        return
    post_search(tree, tree[n][0])
    post_search(tree, tree[n][1])
    print(n, end=" ")


tree = [
    [],
    [2, 3],
    [4, 5],
    [6, 7]
]

print("전위순회 출력 :", end=" ")
pre_search(tree, 1)
print()

print("중위순회 출력 :", end=" ")
in_search(tree, 1)
print()

print("후위순회 출력 :", end=" ")
post_search(tree, 1)