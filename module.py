import sys

print("命令行参数如下：")
for arg in sys.argv:
    print(arg)

print("Python 路径为：", sys.path, "\n")

# 使用 python module.py arg1 arg2 运行