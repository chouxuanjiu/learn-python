"""
Python自学笔记
Day7 19/8/29 字符串和常用数据结构
"""
# 元组tuple / 不能修改
t = ('西瓜', 18, True, '苹果')
print(t)
# 获取元组中的元素
print(t[0]) #西瓜
# 不能给元组元素赋值，否则TypeError:'tuple' object does not support item assignment
"""
t[0] = '香蕉' 
"""
# 只能重新引用新的元组，原来的元组将被垃圾回收
t = ('香蕉', 18, True, '苹果')
print(t) #('香蕉', 18, True, '苹果')
# 或将元组转成列表
person = list(t)
# 然后修改元素
person[0] = '橘子'
person[1] = 81
print(person) #['橘子', 81, True, '苹果']
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#集合
set1 = {1, 9, 9, 8, 2, 3}
print(set1) #{1, 2, 3, 8, 9} 重复的不算
#取长度/个数
print('Length =', len(set1))  #Length = 5
set2 = set(range(1, 10)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set2)
set1.add(4)
set1.add(5)
set2.update([11, 12])
print(set1) #{1, 2, 3, 4, 5, 8, 9}
print(set2) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
set2.discard(5)
# remove的元素如果不存在会引发KeyError
if 4 in set2:
    set2.remove(4)
print(set2)#{1, 2, 3, 6, 7, 8, 9, 11, 12}
# 遍历集合容器
for elem in set2:
    print(elem ** 2, end=' ') #依次求平方
print() #换行
# 将元组转换成集合
set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop()) #1
print(set3) #{2, 3}
# 集合的交集、并集、差集、对称差运算
#set1 = {1, 2, 3, 4, 5, 8, 9}
#set2 = {1, 2, 3, 6, 7, 8, 9, 11, 12}
#set3 = {2, 3}
print(set1 & set2) #交集 {1, 2, 3, 8, 9}
# print(set1.intersection(set2))
print(set1 | set2) #并集 {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
# print(set1.union(set2))
print(set1 - set2) #差集 {4, 5}
# print(set1.difference(set2))
print(set2 - set1) #差集 {11, 12, 6, 7} ？为什么不按顺序排列？
# print(set2.difference(set1))
print(set1 ^ set2) #对称差集 {4, 5, 6, 7, 11, 12}
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))


#字典 / 键与值配对，冒号分开
scores = {'小明': 99, '小美': 47, '小花': 60}
# 通过键，取值
print(scores['小明']) # 99
# 更新字典中的元素
scores['小明'] = 96
scores['小罗'] = 71
scores.update(小明=95, 小悠=88)
print(scores) #{'小明': 95, '小美': 47, '小花': 60, '小罗': 71, '小悠': 88}
if '小悠' in scores:
    print(scores['小悠']) #88
print(scores.get('小悠')) #88
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('小歪', 50)) #50
print(scores) # {'小明': 95, '小美': 47, '小花': 60, '小罗': 71, '小悠': 88}
# 删除字典中的元素
print(scores.popitem()) #('小悠', 88)
print(scores) #{'小明': 95, '小美': 47, '小花': 60, '小罗': 71}
print(scores.popitem()) #('小罗', 71)
print(scores) #{'小明': 95, '小美': 47, '小花': 60}
print(scores.pop('小明', 100)) #95
print(scores) #{'小美': 47, '小花': 60}
# 清空字典
scores.clear()
print(scores) # {}