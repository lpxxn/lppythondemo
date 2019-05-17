#!/usr/bin/env python3
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

# 下面正确
#from init_demo.package_x.sub_b import module_m2
# 使用了.. 相对路径就要在package_x包外执行
# 或者在包外面 使用-m 指定
# python -m package_x.sub_a.module_m1
from ..sub_b import module_m2



def func_X():
    print("hello world x")


# sub_b.fun_B()

def _test():
    module_m2.fun_B()


if __name__ == "__main__":
    _test()