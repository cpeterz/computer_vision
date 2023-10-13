import numpy as np

def custom_dot_product(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    else:
        dot = 0
        for i in range(len(arr1)):
                dot = dot + arr1[i]*arr2[i]
        return dot
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = custom_dot_product(arr1, arr2)
print(result)  # 输出应为 32

arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([4, 5, 6])
result2 = custom_dot_product(arr3, arr4)
print(result2)  # 输出应为 None

arr5 = np.array([])
arr6 = np.array([4, 5, 6])
result3 = custom_dot_product(arr5, arr6)
print(result3)  # 输出应为 None