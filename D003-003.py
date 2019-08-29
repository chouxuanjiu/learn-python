"""
Python自学笔记
Day3 19/8/21 分支结构
"""
#根据天数计算当月交通费
"""
公交：1元/次
地铁：4元/次
优惠：乘客乘车使用市政交通一卡通乘坐轨道交通支出累计满100元后，超出部分给予8折优惠（优惠20%）；
满150元后，超出部分给予5折（优惠50%）优惠；
支出累计达到400元后，不再享受打折优惠
"""
days = int(input('天数：'))
busFare = (1 + 1) * days
if days <= 12:
    metroFare = (4 + 4) * days
    print('当前天数交通费合计%.02f元。' % (busFare + metroFare) )
elif days == 13:
    metroFare = ((4 + 4) * 12) + (4 + (4 * 0.8))
    print('当前天数交通费合计%.02f元。' % (busFare + metroFare) )
elif days <=20:
    metroFare = ((4 + 4) * 12) + (4 + (4 * 0.8)) + ((4 + 4) * 0.8 *(days - 13))
    print('当前天数交通费合计%.02f元。' % (busFare + metroFare) )
elif days == 21:
    metroFare = ((4 + 4) * 12) + (4 + (4 * 0.8)) + ((4 + 4) * 0.8 * (20 - 13)) + ((4 *0.8) + (4 * 0.5))
    print('当前天数交通费合计%.02f元。' % (busFare + metroFare))
elif days <= 31:
    metroFare = ((4 + 4) * 12) + (4 + (4 * 0.8)) + ((4 + 4) * 0.8 * (20 - 13)) + ((4 * 0.8) + (4 * 0.5)) + ((4 + 4) * 0.5 * (days - 21))
    print('当前天数交通费合计%.02f元。' % (busFare + metroFare))
else:
    print('输入天数超过一个月时间。')

