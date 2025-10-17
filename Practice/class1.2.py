import numpy as np

# 创建一个 3x3 的二维数组（内容自定，这里用 1~9）
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("原始矩阵：")
print(arr)

# 输出转置矩阵
print("转置矩阵：")
print(arr.T)
