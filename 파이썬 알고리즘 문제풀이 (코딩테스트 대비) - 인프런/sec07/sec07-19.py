def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while arr[pivot] >= arr[left] and left < end:
            left += 1
        print(left, right)
        while arr[pivot] <= arr[right] and right > start+1:
            right -= 1
            print(right)
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            break
    print("정렬", start+1, end+1, list(arr))
    quick_sort(start, right-1)
    quick_sort(right+1, end)


#arr = [23, 11, 45, 36, 15, 67, 33, 21]
arr = [1,3,4,7,78,5,3,2,4,7,8]
print(arr)
quick_sort(0, len(arr)-1)
print(arr)