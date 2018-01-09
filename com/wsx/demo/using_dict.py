# 字典类似map，创建键值对类型
# 'ab' is short for 'a'dress'b'ook
ab = {
    'Swaroop':'swaroopcn@byteofpython.info',
    'Larry':'lary@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}
# 通过键名称打印对应值内容
print("Swaroop's address is %s" % ab['Swaroop'])

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

# 输出字典长度，通过字典的items方法循环打印键值对元素
print('\nThere are %d contacts in the address book\n' % len(ab))
for name, address in ab.items():
    print('Contact %s at %s' % (name, address))

# 如果字典中有键名称为'Guido'，打印指定内容
if 'Guido' in ab:  # OR ab.has_key(Guido)
    print("\nGuido's address is %s" % ab['Guido'])