"""
Python自学笔记
Day6 19/8/26 字符串和常用数据结构
"""
def main():
    #关于字符串
    str1 = 'hello,world!'
    # 通过len函数计算字符串的长度
    print(len(str1))  # 12
    # 切片，正向从左开始，第1个元素对应下标为0，反向从右开始，第1个元素对应下标为-1
    print(str1[0:5]) # hell0，即下标0到5之前，不包括5
    # 取出指定位置的字符
    print(str1[5])  # ,
    print(str1[2:5])  # llo 2到5之前
    print(str1[2:])  # llo,world! 2到末尾
    print(str1[2::2])  # lowrd 2到末尾，步长2
    print(str1[::2])  # hlowrd 0到末尾，步长2
    print(str1[::-1])  # !dlrow,olleh -1到末尾，步长1
    print(str1[-3:-1])  # ld 右向左第3个到第1个，不包括第1个
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(20, '*')) # ****hello,world!****

    #关于列表
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    # 计算列表长度(元素个数)
    print(len(list1)) # 5
    # 下标/索引
    print(list1[0]) # 1
    print(list1[4]) # 100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1]) # 100
    print(list1[-3]) # 5
    # 替换
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]
    # 添加
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1) # [1, 400, 3, 300, 7, 100, 200, 1000, 2000]
    print(len(list1)) # 9
    # 删除
    list1.remove(3)
    if 1000 in list1:
        list1.remove(1000)
    del list1[0]
    print(list1) # [400, 300, 7, 100, 200, 2000]
    # 清空
    list1.clear()
    print(list1) # []

if __name__ == '__main__':
    main()