# 下面是正确的
# from init_demo.package_y.sub_a import module_m1
# 使用了.. 相对路径就要在package_x包外执行
# 或者在包外面 使用-m 指定
# python -m package_y.sub_b.module_m2
from ..sub_a import module_m1
module_m1.func_X()


def func_b_q():
    print("bq")


def fun_B():
    print("hello func B!")


if __name__ == "__main__":
    fun_B()
    func_b_q()
