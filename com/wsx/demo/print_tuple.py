# 元组由于创建之后不能改变的特性，通常用于打印语句
age = 22
name = "Jackson"
# 格式化输出打印，%s表示字符，%d表示数字，分别对应元组中的数据类型
print('%s is %d years old' % (name, age))
# 当print函数中元素只有一个时可以定制，即省略括号
print('Why is %s playing with that python?' % name)