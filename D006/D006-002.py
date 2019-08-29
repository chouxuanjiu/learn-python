"""
Python自学笔记
Day6 19/8/24 函数和模块的使用
"""
def main():
    # Todo: Add your code here
    # 实现计算求最大公约数和最小公倍数的函数

    def GCD(x, y):
        # 最大公约数Greatest Common Divisor
        if x > y:
            x, y = y, x
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return factor

    def LCM(x, y):
        # 最小公倍数Least Common Multiple
        if x > y:
            x, y = y, x
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return x * y // factor

    a = int(input('a = '))
    b = int(input('b = '))
    print('x,y的最大公约数是：', GCD(a, b))
    print('x,y的最小公倍数是：', LCM(a, b))

    # 实现判断一个数是不是回文数的函数
    def isPalindrome(num):
        temp = num
        num2 = 0
        while temp > 0:
            num2 *= 10
            num2 += temp % 10
            temp //= 10
        return num == num2

    c = int(input('c = : '))
    print('是否回文数:', isPalindrome(c))

    # 实现判断一个数是不是素数的函数

    def isPrimeNumber(num):
        from math import sqrt
        end = int(sqrt(num))
        is_prime = True
        for _ in range(2, end + 1):
            if num % _ == 0:
                is_prime = False
                break
        return is_prime

    d = int(input('d = '))
    print('是否是素数:', isPrimeNumber(d))

    # 判断输入的正整数是不是回文素数

    e = int(input('e = '))
    print('是否是回文素数：', isPalindrome(e) and isPrimeNumber(e))
    pass

if __name__ == '__main__':
    main()
