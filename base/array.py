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
    # 第二个为空,表示
