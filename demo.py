# 对列表进行永久性排序（根据字符进行排序）
cars = ['bom', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# 对列表进行反序排序
# cars.reverse()
# print(cars)

# 查看列表的长度
print(len(cars))

# 遍历列表信息
# for car in cars:
#     print(car.title())
# print("列表输出完毕")

# 创建列表
# for i in range(1, 11):
#     print(i)

# 顺序生成列表
numbers = list(range(1, 6))
print('输出的列表结果为:', numbers)

# 简单的列表统计计算
# number_demo = [1, 23, 34, 4, 534, 23]
# print(max(number_demo))
# print(min(number_demo))
# print(sum(number_demo))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 切片
print(cars[0:2])  # 输出的时列表的1~2个元素
print(cars[0:-3])  # 输出倒数列表第4个元素
print(cars[:2])  # 输出前两个元素
# 遍历切片 ->输出前两位元素
for car in cars[:2]:
    print(car)

# 复制列表
# 第一种复制方式
car_plus = cars
cars.append('beijing')
car_plus.append('chang_an')
print(car_plus)
print(cars)
# 验证结果说明，该复制方法是让另一个列表，和被复制对象指向同一个存储空间

# 第二种复制方式
car_plus = cars[:]
cars.append('beijing')
car_plus.append('chang_an')
print(car_plus)
print(cars)
# 验证结果说明，该复制方法是让另一个列表，和被复制对象指向不同的存储空间

