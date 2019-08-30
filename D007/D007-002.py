"""
Python自学笔记
Day7 19/8/26 字符串和常用数据结构
"""
import sys

def main():
    # 列表排序
    list1 = ['orange', 'apple', 'melons', 'peach', 'blueberry','banana','cherry','pear','grape']
    # sorted函数返回列表排序后的拷贝/按字母，不会修改传入的列表
    list2 = sorted(list1)
    # reverse倒序
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)

    #创建列表
    f = [x for x in range(1, 10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f)

    f = [x + y for x in 'ABCDE' for y in '1234567'] # ['A1', …… 'A7', 'B1', …… 'B7', 'C1',…… 'E7']
    print(f)

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数，9032
    print(f) # [1, 4, 9, ……998001]

    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间，128
    print(f) # <generator object main.<locals>.<genexpr> at 0xfff5a8fbd0>
    for val in f:
        print(val, end=',') # 1,4,9,……998001,

if __name__ == '__main__':
    main()