"""
Python自学笔记
Day5 19/8/23 构造程序逻辑
"""
"""
lily.py\找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""
#myself
for a in range (1,10):
    for b in range (10):
        for c in range (10):
            if (100 * a) + (10 * b) + c == (a ** 3) + (b ** 3) + (c ** 3):
                print(((100 * a) + (10 * b) + c),end=' ')

#GitHub
for num in range(100, 1000):
    low = num % 10
    #%为取余，%10等于取最后一位个位数
    mid = num // 10 % 10
    #//为取商，//10等于取个位之前的所有数
    high = num // 100
    #//10等于取十位之前的所有数
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)