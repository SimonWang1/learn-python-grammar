age = 20
name = 'Tom'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
# 对于小数点'0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，保持文本处于中间位置
# 使用(^)定义'___hello___'长度为11
print('{0:_^11}'.format('hello'))
# 基于关键词输出'Tom wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Tom', book='A Byte of Python'))
