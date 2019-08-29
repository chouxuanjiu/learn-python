"""
Python自学笔记
Day2 19/8/20 语言元素
"""
#练习题：输入圆的半径计算周长和面积
import math

r = float(input('请输入圆的半径(cm)='))
l = 2 * math.pi * r
s = math.pi * r * r
print('半径为%.02fcm的圆，周长为%.02fcm，面积为%.02fcm^2' % (r,l,s))