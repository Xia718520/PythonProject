import numpy as np

# 定义两个 2x2 矩阵
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 矩阵加法
add_result = A + B

# 矩阵减法
sub_result = A - B

# 找最大值和最小值
max_val = np.amax([A, B])  # 在两个矩阵中找最大值
min_val = np.amin([A, B])  # 在两个矩阵中找最小值

print("矩阵 A:\n", A)
print("矩阵 B:\n", B)

print("\nA + B =\n", add_result)
print("\nA - B =\n", sub_result)

print("\n两个矩阵中的最大值:", max_val)
print("两个矩阵中的最小值:", min_val)
