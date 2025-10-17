'''
字符串类型不同的是，bytes 类型中的元素是整数值
创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：

x = bytes("hello", encoding="utf-8")
此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
'''

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

#需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")