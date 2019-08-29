"""
Python自学笔记
Day5 19/8/23 构造程序逻辑
"""
"""
palindrome.py\判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""
num = int(input('请输入一个正整数: '))
temp = num
#保留num以待比较，计算temp
num2 = 0
while temp > 0:
    num2 *= 10
    #整体进一位
    num2 += temp % 10
    #%取余数，%10等于取最后个位的数
    temp //= 10
    #//取商，//10等于取个位之前的数
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
