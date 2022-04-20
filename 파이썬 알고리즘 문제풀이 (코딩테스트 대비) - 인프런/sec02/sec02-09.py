# 실패!
# 말도 안되게 어렵게 풀었음.
# 깊이 반성할 것.

result = []
count = {}

c = int(input())
for i in range(c):
    nums = list(map(int, input().split()))
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    dice_list = list(count.items())
    dice_list.sort(key=lambda x: x[1], reverse=True)
    if dice_list[0][1] == 3:
        money = 10000 + dice_list[0][0] * 1000
        result.append(money)
    elif dice_list[0][1] == 2:
        money = 1000 + dice_list[0][0] * 100
        result.append(money)
    else:
        dice_list.sort(reverse=True)
        money = dice_list[0][0] * 100
        result.append(money)

final_result = max(result)
print(final_result)
