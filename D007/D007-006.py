"""
Python自学笔记
Day7 19/8/31 字符串和常用数据结构
"""

#定义函数，生成4位验证码

import random

def generate_code(code_len=4): #默认验证码4个字符
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1 # len(all_chars)=62，字符下标应从0至61
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos) #随机从0到待选字符串长之间选数
        code += all_chars[index] #用上行的随机数从待选字符串里指定字符
    return code

print(generate_code())
