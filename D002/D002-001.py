"""
Python自学笔记
Day2 19/8/20 语言元素
"""
#变量类型和运算符

a = int(input('输入数字a='))
b = int(input('输入数字b='))
# int()转换为整数类型
print('%d + %d = %d' % (a, b, a+b))
print('%d ** %d = %d' % (a, b, a**b))
print('%d // %d = %d' % (a, b, a//b))
# %标记格式转换说明符，d表示带符号的十进制整数

a = 5
b = 4
c = 3
d = 2
e = 1
a += b
a -= c
a *= d
a /= e
print("a = ", a)



flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)