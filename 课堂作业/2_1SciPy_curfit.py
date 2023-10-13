import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a * x * x * x + b * x * x + c * x + d

def fit_polynomial(data):
    p0 = [0.1,0.6,1.0,0.0]
    try:
        popt, pcov = curve_fit(func, data[:, 0], data[:, 1], p0)
        return popt
    except RuntimeError as e:
        print(f"拟合失败: {e}")
        return None

# 生成一组模拟数据
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.1, 0.9, 2.2, 4.0, 7.0])
data = np.vstack((x, y)).T

coefficients = fit_polynomial(data)
print(coefficients)  # 输出应为 [0.1, 0.6, 1.0, 0.0] 或类似结果