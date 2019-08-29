"""
Python自学笔记
Day4 19/8/22 循环结构
"""
#while循环，猜数字版本2

import random
number = random.randint(1, 100)
guessesTaken = 0
while True:
    guessesTaken += 1
    usrAnswer = int(input('答案应该是：'))
    if usrAnswer < number and guessesTaken < 7:
        print('嗯，你猜的数小了点')
    elif usrAnswer > number and guessesTaken < 7:
        print('喔，你猜的数太大了')
    elif usrAnswer != number and guessesTaken >= 7:
        print('抱歉，机会用完了，你还是没能猜对。我想到的数字是%d。' % (number))
        break
    else:
        print('干得好！你猜中了我想的数字。')
        break
print('你总共猜了%d次。' % guessesTaken)
