'''
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
a = b = c = 1
print(a)
print(b)
print(c)
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)
#以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

# 变量定义
x = 10          # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_active)) # <class 'bool'>