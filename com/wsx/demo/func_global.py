def func():
    # global声明变量为全局变量
    global x
    print('x is', x)
    x = 2
    print('Changed local x to', x)


x = 50
# 将全局变量更改为固定值并打印
func()
print('value of x is', x)