"""
Python自学笔记
Day5 19/8/23 构造程序逻辑
"""
"""
chicken.py\求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""
#myself
for roosterNo in range(20):
    for henNo in range(33):
        for chickNo in range(100):
            roosterCost = roosterNo * 5
            henCost = henNo * 3
            chickCost = chickNo * 1 / 3
            if roosterCost + henCost + chickCost == 100 and roosterNo + henNo + chickNo == 100:
                print('公鸡有%d只，母鸡有%d只，小鸡有%d只。' % (roosterNo,henNo,chickNo))

#GitHub
for roosterNo in range(0, 20):
    for henNo in range(0, 33):
        chickNo = 100 - roosterNo - henNo
        if 5 * roosterNo + 3 * henNo + chickNo / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (roosterNo,henNo,chickNo))