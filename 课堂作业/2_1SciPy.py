import numpy as np
from scipy.stats import normaltest

def check_normality(data):
    statistic, p_value = normaltest(data)
    if p_value < 0.05:
        result = "数据不满足正态分布假设"
    else:
        result = "数据满足正态分布假设"

    return result

# 生成一组模拟数据（这里使用正态分布的数据）
data1 = np.random.normal(0, 1, 100)
result1 = check_normality(data1)
print(result1)  # 输出应为 "数据服从正态分布"

# 生成一组不服从正态分布的数据（这里使用均匀分布的数据）
data2 = np.random.uniform(0, 1, 100)
result2 = check_normality(data2)
print(result2)  # 输出应为 "数据不服从正态分布"