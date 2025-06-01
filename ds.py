# 转置矩阵
matrix = [[1, 2, 3,4], 
          [5, 6, 7,8], 
          [9, 10, 11,12]]

# 第一种方式：
new_matrix = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    new_matrix.append(new_row)
print(new_matrix)  # Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 第二种方式：使用列表推导式
new_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(new_matrix)  # Output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 元组
# 定义方式：
t1 = (1, 2, 3)
print(type(t1))  # <class 'tuple'>
t2 = 1, 2, 3  # 自动推断为元组
print(type(t2))  # <class 'tuple'>

# 集合
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # Output: {'orange', 'banana', 'pear', 'apple'}
print("orange" in basket)  # Output: True

a = set("abracadabra")
b = set("alacazam")
print(a)  # Output: {'a', 'b', 'c', 'd', 'r'}
print(b)  # Output: {'a', 'c', 'l', 'm', 'z'}
print(a - b)  # 差集: {'b', 'd', 'r'}

# 字典
a = {'name': 'Alice', 'age': 30, 'city': 'New York'}
a = dict([('name', 'Alice'), ('age', 30), ('city', 'New York')])  # 使用 dict() 函数从键值对元组创建字典
a = dict(name='Alice', age=30, city='New York')  # 使用 dict() 函数创建字典
print(list(a.keys()))  # Output: ['name', 'age', 'city']
print(sorted(a.keys()))  # Output: ['age', 'city', 'name']
print(list(a.values()))  # Output: ['Alice', 30, 'New York']
for k,v in a.items():
    print(f"{k}: {v}")  # 输出每个键值对

a = ['name', 'age', 'city']
b = ['Alice', 30, 'New York']
z = zip(a, b)  # 将两个列表打包成一个迭代器
print(type(z))  # <class 'zip'>
for k, v in z:
    print(f"{k}: {v}")  # 输出每个键值对