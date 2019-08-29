"""
Python自学笔记
Day5 19/8/23 构造程序逻辑
"""
"""
fibonacci.py\输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 34...
"""
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')