import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

# 设置负号正常显示
plt.rcParams['axes.unicode_minus'] = False

print("Matplotlib环境配置完成！")
# 创建数据
x = np.arange(1, 10)  # 生成1到9的数组
y = 2 * x  # y = 2x

# 绘制线状图
plt.figure(figsize=(8, 6))
plt.title("线性关系图")
plt.xlabel("x 轴")
plt.ylabel("y 轴")
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 生成随机数据
np.random.seed(42)  # 设置随机种子确保结果可重现
x = np.random.randn(1000)  # 1000个正态分布随机数
y = np.random.randn(1000)  # 1000个正态分布随机数

# 绘制散点图
plt.figure(figsize=(8, 6))
plt.title("随机散点图")
plt.xlabel("x 轴")
plt.ylabel("y 轴")
plt.scatter(x, y, c='blue', alpha=0.6, s=20)  # s控制点的大小
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()

# 准备数据
x = [1, 4, 7]    # 第一组柱状图的x坐标
y = [2, 5, 8]    # 第一组柱状图的高度
x2 = [3, 6, 9]   # 第二组柱状图的x坐标
y2 = [8, 7, 4]   # 第二组柱状图的高度

# 绘制柱状图
plt.figure(figsize=(8, 6))
plt.bar(x, y, align='center', width=0.8, color='blue', alpha=0.7, label='组一')
plt.bar(x2, y2, align='center', width=0.8, color='red', alpha=0.7, label='组二')
plt.title('双组柱状图对比')
plt.ylabel('Y 坐标')
plt.xlabel('X 坐标')
plt.legend()  # 显示图例
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()

# 创建2行1列的子图布局
fig = plt.figure(figsize=(10, 8), dpi=100)

# 第一个子图：线状图
x1 = np.arange(1, 10)
y1 = 2 * x1
plt.subplot(2, 1, 1)  # 2行1列，第1个位置
plt.plot(x1, y1, 'b-', linewidth=2)
plt.title('线状图示例')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.grid(True, linestyle='--', alpha=0.5)

# 第二个子图：散点图
x2 = np.arange(1, 10)
y2 = 2 * x2 + np.random.randn(9)  # 添加随机噪声
plt.subplot(2, 1, 2)  # 2行1列，第2个位置
plt.plot(x2, y2, 'ro', markersize=6)
plt.title('散点图示例')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()  # 自动调整子图间距
plt.show()