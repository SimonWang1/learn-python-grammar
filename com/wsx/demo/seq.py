shop_list = ['apple', 'carrot', 'mango', 'banana']
# 使用索引操作符通过列表下标查找元素并打印
print('Item 0 is', shop_list[0])
print('Item 1 is', shop_list[1])
print('Item 2 is', shop_list[2])
print('Item 3 is', shop_list[3])
# 下标'-1'表示列表最后一个元素
print('Item -1 is', shop_list[-1])
print('Item -2 is', shop_list[-2])

# 使用切片操作符切割列表元素并打印，其中范围包含左侧不包含右侧，即'[ )'
print('Item 1 to 3 is', shop_list[1:3])
# 左右单独无内容表示从开头或到结尾
print('Item 2 to end is', shop_list[2:])
print('Item start to -1 is', shop_list[:-1])
# 无内容表示从头到尾
print('Item start to end is', shop_list[:])

# 试用切片操作符切割字符串并打印
name = 'swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])