"""
Python自学笔记
Day7 19/8/26 字符串和常用数据结构
"""
# 通过yield关键字将普通函数改造成生成器函数

#简单输入斐波那契數列前 N 个数
print('版本1')
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fab(5)

#为提高fab函数的可复用性，最好不要直接打印出数列，而是返回一个 List
print('版本2')
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

for n in fab(5):
    print(n)

#为控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代
#iterable即可迭代对象，是能够一次返回其一个成员的对象
print('版本3')
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    def __iter__(self):
        return self
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
for n in Fab(5):
    print(n)

#使用yield,保持第一版的简洁性，同时获得iterable的效果
print('版本4')
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield，第一版为print b
        a, b = b, a + b
        n = n + 1
for n in fab(5):
    print(n)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a #yield和return的区别。yield可以向下运行。而return返回后这个函数余下的部分就不能执行了

for val in fib(5):
    print(val,end=',')

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

"""
1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
4.程序执行print("*"*20)，输出20个*
5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.
到这里你可能就明白yield和return的关系和区别了，带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。

"""