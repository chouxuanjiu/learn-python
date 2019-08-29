"""
Python自学笔记
Day4 19/8/22 循环结构
"""
#for-in循环，1～100偶数求和
sum = 0
for x in range(2,101,2):
#range(start,stop,step)创建整数序列，start默认0，stop不包括stop本身
    sum += x
print('1~100之间的偶数之和等于：%d' % (sum))

#for-in循环，1～100偶数求和，分支结构
sum = 0
for x in range(1,101):
    if x % 2 == 0:
        sum += x
print('1~100之间的偶数之和等于：%d' % (sum))

