# 使用列表数据类型list，理解成不定长可变类型数组，使用方括号定义逗号分隔
# 创建一个购物列表
shop_list = ['apple', 'mango', 'carrot', 'banana']
# 逗号消除自带换行符
print('I have', len(shop_list), 'item to purchase.')
print('This items are:')  # Notice comma at the end of line
for item in shop_list:
    print(item)

print('\nI also have to buy rice.')
# 使用append方法添加元素
shop_list.append('rice')
print('My shopping list is now', shop_list)

print('I will sort my list now')
# 使用sort方法按首字母顺序进行排序
shop_list.sort()
print('Sorted shopping list is', shop_list)

print('The first item i will buy is', shop_list[0])
old_item = shop_list[0]
# 使用del方法对列表下表为0的元素进行删除
del shop_list[0]
print('I bought the', old_item)
print('My shopping list is now', shop_list)
