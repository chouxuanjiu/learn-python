"""
Python自学笔记
Day6 19/8/24 函数和模块的使用
"""
#摇色子
from random import randint
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

print(roll_dice())
print(roll_dice(3))

#相加，*表示可变参数，可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1, 3, 5, 7, 9))

#加法计算器
inputList = input('请输入要相加的数，用空格隔开：')
numberList = inputList.split(' ')
def sum(list):
	result = 0
	for x in list:
		result += float(x)
	return result
print(sum(numberList))