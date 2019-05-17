# 报错 这样的语句会导入哪些文件取决于操作系统的文件系统. 所以我们在__init__.py 中加入 __all__变量.
#from package_y import *
from package_y.sub_b import *


module_m2.func_b_q()
