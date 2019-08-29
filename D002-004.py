"""
Python自学笔记
Day2 19/8/20 语言元素
"""
#练习题：判断闰年（四年一闰；百年不闰，四百年再闰）
Year = int(input("请输入年份：") )
LeapYear = (Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0)
# %取模/返回余数，==等于，!=不等于
if LeapYear == False:
    print('恐怕%d年并不是闰年。' % Year )
else:
    print('是的，%d年是闰年没错。' % Year )


