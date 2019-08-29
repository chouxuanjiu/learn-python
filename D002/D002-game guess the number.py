"""
Python自学笔记
Day2 19/8/20 “猜数字”
——计算机想到一个 1 到 20 之间的随机数,让你来猜它是几。
计算机会告诉你每次猜的数太大还是太小。
如果能够在 6 次之内猜到正确的数字,就赢得游戏。
"""
import random
number = random.randint(1, 20)
# random.randint()生成随机整数

usrName = input('你好，请问你怎么称呼：')
print('欢迎光临%s，让我们一起玩个游戏吧！下面我来随便想个整数，在1到20之间。' % (usrName))
# %s表示字符串

guessesTaken = 0
guessesLeft = 6

while guessesTaken < 6:
    print('请你来猜猜我想到的数字吧！')
    usrGuess = int(input('答案应该是：'))
    guessesTaken = guessesTaken + 1
    guessesLeft = guessesLeft - 1
    if usrGuess < number:
        print('嗯，你猜的数小了点，你还有%d次机会，加油。' % (guessesLeft))
    if usrGuess > number:
        print('喔，你猜的数太大了，你还有%d次机会，加油。' % (guessesLeft))
    if usrGuess == number:
        break
#用缩进来设置代码层次

if usrGuess == number:
    print('干得好，%s！你猜中了我想的数字，共用了%d次机会。' % (usrName,guessesTaken))
if usrGuess != number:
    print('抱歉，机会用完了，你还是没能猜对。我想到的数字是%d。' % (number))