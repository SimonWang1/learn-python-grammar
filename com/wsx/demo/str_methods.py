# 创建一个字符串
name = 'Swoop'
# 判断字符串是否以某个元素开始
if name.startswith('Swoo'):
    print('Yes, the string starts with "Swoo"')
# 判断字符串是否包含某元素
if 'a' in name:
    print('Yes, it contains the string "a"')
# 判断的另一个方式
if name.find('woo') != -1:
    print('Yes, it contains the string "woo"')
# 字符串连接列表中的元素创建新的字符串
delimiter = '_*_'
my_list = ['Brazil', 'India', 'Russia', 'China']
print(delimiter.join(my_list))