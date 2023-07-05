# https://www.runoob.com/python3/python3-data-type.html

list = ['a', 'b', 123, 'c', 'd']
print(list)

print(list[0])
print(list[1:3])
print('[2:]', list[2:])
print('[2:-1]', list[2:-1])
print('[-2:]', list[-2:])

# 将 [2:4] 设置为[]
list[2:4] = []
print('将 [2:4] 设置为[]', list, ' len:', len(list))


def reverseWord(input):
    # 通过空格分词
    inputWords = input.split(' ')
    # 翻转字符串
    # 假设列表 list = [1, 2, 3, 4]
    # list[0] = 1, list[1]=2, -1 表示最后一个 list[-1]=4( equals list[3] = 4)
    # inputWords[-1::-1] 有三个元素
    # 第一个参数-1 表示最后一个元素
    # 第二个为空,表示 移到到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    output = ' '.join(inputWords)
    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWord(input)
    print(rw)

print("----元组----")
# 元组与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号，列表使用方括号。
tuple = ('a', 'b', 123, 'c', 'd')
print(tuple)
# 一个元素，需要在元素后添加逗号，否则括号会被当作运算符使用，因为括号既可以表示 tuple，又可以表示数学公式中的小括号
tuple = (1,)
print(type(tuple))
print(tuple)
tuple = (1)
print(tuple)
print(type(tuple))
# 空元组, 不能省略括号
tuple = ()
print(tuple)
print(type(tuple))

# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，不能使用{}创建空集合，{}只能创建空字典
# 创建空集合
s = set()
print(type(s))
print(s)

# 创建非空集合
s = {'a', 'b', 123, 'c', 'd'}
print(type(s))
print(s)
s = set('abc123')
print(type(s))
print(s)