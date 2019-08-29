"""
Python自学笔记
Day4 19/8/22 循环结构
"""
#用*打印三种形状的三角形
row = int(input('请输入三角形行数: '))

for i in range(row):
    for _ in range(i + 1):
    #习惯用_作丢弃变量，非标准
        print('*', end='')
        #end=''不换行
    print()
    #换行


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

for i in range(row):
    print(('*' * (i * 2 - 1)).center(row * 2 - 1))



#用*打印菱形
for i in range (2 * row - 1):
    if i < row:
        number = 2 * i + 1
    else:
        number = 2 * (2 * row - 1 - i) - 1
    print(('*' * number).center(2 * row - 1))
#print(a.center(x,'y'))表示让字符串a占位x个位置，剩余的位置用‘y’填充，默认为空格