"""
Python自学笔记
Day3 19/8/21 分支结构
"""
#输入三条边长如果能构成三角形就计算周长和面积
import math

a = float(input('请输入三角形A边长：'))
b = float(input('请输入三角形B边长：'))
c = float(input('请输入三角形C边长：'))
if a + b > c and b + c > a and c + a > b:
    print('当三角形三边长分别为%.02f、%.02f、%.02f时，该三角形周长为%.02f。' % (a,b,c,a + b + c))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    #math.sqrt()计算平方根
    print('当三角形三边长分别为%.02f、%.02f、%.02f时，该三角形面积为%.02f。' % (a,b,c,s))
else:
    print('抱歉，以上三条边长无法构成三角形。')