print('Simple Assignment')
shop_list = ['apple', 'banana', 'mango', 'grape']
# my_list和shop_list参考（指向）同一个对象只是换了名字
my_list = shop_list

del shop_list[0]
# 因为两个参考同一个对象，所以删除一个元素打印出相同的结果
print('shop_list is', shop_list)
print('my_list is', my_list)

print('Copy by making a full slice')
# 使用切片操作符做完全复制
my_list = shop_list[:]
# 删除第一个元素
del my_list[0]
# 因为复制了新的对象内容，所以删除一个元素打印不同的结果
print('shop_list is', shop_list)
print('my_list is', my_list)