import numpy as np

def custom_median(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    # if len(arr)%2 == 0:
    #     return (arr[(len(arr)/2 - 1)] + arr[(len(arr)/2)])/2
    # else:
    #     return arr[(len(arr) - 1)/2]

    if len(arr) % 2 == 0 and len(arr) > 0:
        middle1 = arr[(len(arr) // 2 - 1)]
        middle2 = arr[(len(arr) // 2)]
        return (middle1 + middle2) / 2
    elif len(arr) % 2 == 1 and len(arr) > 0:
        return arr[(len(arr) // 2)]
    else:
        return None



arr1 = np.array([1, 3, 2, 6, 5, 4])
result1 = custom_median(arr1)
print(result1)  # 输出应为 3.5

arr2 = np.array([10, 9, 8, 7, 6])
result2 = custom_median(arr2)
print(result2)  # 输出应为 8.0

arr3 = np.array([])
result3 = custom_median(arr3)
print(result3)  # 输出应为 None