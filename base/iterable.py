# 常见的可迭代对象
from collections.abc import Iterable

iterables = [
    "123",  # 字符串
    [1, 2, 3],  # 列表
    (1, 2, 3),  # 元组
    {1: 'a', 2: 'b', 3: 'c'},  # 字典
    {'a', 'b', 'c'},  # 集合
]

for iterable in iterables:
    print("========+++++++++++++========")
    print(f"{iterable} is iterable: {isinstance(iterable, Iterable)}")
    print(f"type({iterable}) is {type(iterable)}")
    for x in iterable:
        print(x, end=", ")
    print('')


def common_attrs(*objs):
    """获取多个对象的公共属性"""
    assert len(objs) > 0, "至少需要一个对象"
    "dir 返回一个对象的属性列表"
    attrs = set(dir(objs[0]))
    print(attrs)
    for obj in objs[1:]:
        attrs &= set(dir(obj))  # 取交集
    attrs -= set(dir(object))  # 去掉 object 类的属性
    return attrs


print(common_attrs(*iterables))
