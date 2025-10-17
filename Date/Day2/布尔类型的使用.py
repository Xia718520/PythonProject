# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))  # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2)  # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
    '''
    布尔类型只有两个值：True 和 False。

    bool 是 int 的子类，因此布尔值可以被看作整数来使用，其中 True 等价于 1。

    布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0。

    布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。

    布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。

    可以使用 bool() 函数将其他类型的值转换为布尔值。
    以下值在转换为布尔值时为 False：None、False、零 (0、0.0、0j)、空序列（如 ''、()、[]）和空映射（如 {}）。其他所有值转换为布尔值时均为 True。
    
    
    在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，
    只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。
    '''