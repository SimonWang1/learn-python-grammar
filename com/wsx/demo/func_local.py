def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


# 局部变量在块内有效，与函数外的变量没有关系
x = 50
func(x)
print('x is still', x)