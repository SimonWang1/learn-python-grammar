# 使用元组数据类型tuple，理解成字符串，使用圆括号定义逗号分隔，创建之后不能改变
zoo = ('elephant', 'wolf', 'penguin')
print('Number of animals in the zoo is', len(zoo))

# 元组包含格式，使用索引运算符[]查找元素，二维索引查找被包含的元素
new_zoo = ('monkey', 'dolphin', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])