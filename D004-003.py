"""
Python自学笔记
Day4 19/8/22 循环结构
"""

#循环嵌套，九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
        #end='t'以制表符结尾，不换行
    print()
    #默认换行

#输入两个正整数计算最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0 and factor !=1:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
    elif x % factor == 0 and y % factor == 0 and factor ==1:
        print('%d与%d互质' % (x, y))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break