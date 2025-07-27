# num = float(input("Enter a number to find its square root: "))
# num_sqrt = num**0.5  # ** 只适用于正数
# print(f"The square root of {num} is {num_sqrt}")

import cmath

num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print("{0} 的平方根为 {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.imag, num_sqrt.real))
