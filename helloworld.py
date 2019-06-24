import RandomNumberGenerator as W
import time


print("Hello")

def imperative_merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def imperative_merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = imperative_merge_sort(left)
    right = imperative_merge_sort(right)
    return list(imperative_merge(left, right))

def Run_Test(str):
    print("Step 1")
    arr=W.LoadList(str)
    print("Step 2")
    print(arr)
    arr=arr[0]
    start=time.time()
    arr=imperative_merge_sort(arr)
    end=time.time()
    print("Time Taken: ")
    print(end-start)
    print(" Sorted Array:")
    print(arr)

print(imperative_merge_sort([4,5,2,3]))