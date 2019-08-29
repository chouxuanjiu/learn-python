"""
Python自学笔记
Day5 19/8/23 构造程序逻辑
"""
"""
craps.py\Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""
"""
import random
moneyLeft = 1000
print('你一共有%d块赌注。' % moneyLeft)

while True:
    # 下注金额如果超过剩余金额就循环，要求重新输入下注金额
    debt = int(input('请输入下注金额: '))
    if 0 < debt <= moneyLeft:
        break
        # 下注金额如果小于剩余金额就正常往下走，跳出此循环

firstDiceNo = random.randint(1, 6) + random.randint(1, 6)
print('玩家摇出了%d点……' % firstDiceNo)

if firstDiceNo == 7 or firstDiceNo == 11:
    moneyLeft += debt
    print('恭喜你获胜!你的赌注还有%d块。' % moneyLeft)
elif firstDiceNo == 2 or firstDiceNo == 3 or firstDiceNo == 12:
    moneyLeft -= debt
    print('抱歉，这局庄家胜。你的赌注还有%d块。' % moneyLeft)

while moneyLeft > 0:
    while True:
        # 下注金额如果超过剩余金额就循环，要求重新输入下注金额
        debt = int(input('请输入下注金额: '))
        if 0 < debt <= moneyLeft:
            break
            # 下注金额如果小于剩余金额就正常往下走，跳出此循环

    newDiceNo = random.randint(1, 6) + random.randint(1, 6)
    print('玩家摇出了%d点……' % newDiceNo)
    if newDiceNo == 7:
        firstDiceNo = newDiceNo
        moneyLeft -= debt
        print('抱歉，这局庄家胜。你的赌注还有%d块。' % moneyLeft)
    elif newDiceNo == firstDiceNo:
        firstDiceNo = newDiceNo
        moneyLeft += debt
        print('恭喜你获胜!你的赌注还有%d块。' % moneyLeft)
    else:
        firstDiceNo = newDiceNo

print('你已经输光了赌注, 游戏结束!')
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')