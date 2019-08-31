"""
Python自学笔记
Day7 19/8/30 字符串和常用数据结构
"""
#文字跑马灯

import os
import time

content = '北京欢迎你为你开天辟地…………' #字符串变量
while True:
    # 清理屏幕上的输出
    os.system('cls')  # os.system('clear')
    print(content)
    # 休眠200毫秒
    time.sleep(0.2)
    content = content[1:] + content[0] #把字符串第一位挪到最后显示