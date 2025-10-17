"""
运算符	逻辑表达式	描述	实例
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
"""
# 实例1：
a = 10
b = 20
c = 0
d = 5

# 逻辑运算符 and
print(a and b)  # 20
print(a and c)  # 0
print(a and d)  # 5

# 逻辑运算符 or
print(a or b)  # 10
print(a or c)  # 10
print(a or d)  # 10

# 逻辑运算符 not
print(not a)  # False
print(not b)  # False
print(not c)  # True
print(not d)  # False