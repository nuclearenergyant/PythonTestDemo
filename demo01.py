# 元组的测试
dimension = (1, 2)
print( dimension[0] )
# 修改元组元素——》软件会提醒不能修改

# 条件语句测试
my_name = 'Tom'
print( my_name == 'tom' )

num = 17
if num != 18:
    print( 'you are a young boy' )
else:
    print( 'you are a man' )

# 查看特定值是否在列表中
names = ['Tom', 'jon', 'killy']
print( 'Tom' in names )
# 检查特定值是否不包含在列表总
print( 'dell' not in names )

# if语句
# age = 5
# if age > 10:
#     print("你是一个少年了")
# elif 5 < age <= 10:
#     print("你是一个大宝宝")
# else:
#     print("你是一个小宝宝")


# 字典
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0['x'] = 25
# alien_0['y'] = 5
# print(alien_0)
#
# alien_0['x'] = 3
# print(alien_0)

# 遍历字典中的元素
# for key, value in alien_0.items():
#     print("key=" + key)
#     print("value=" + str(value))

# 遍历字典中的所有键
# for key in alien_0.keys():
#     print(key)


# 在字典中存储列表
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese']
# }
# print("你要点的pizza中有：" + pizza['crust'])
# for topping in pizza['toppings']:
#     print(topping)

# 在字典中存储字典
# user = {
#     'demo01': {
#         'first': 'id01',
#         'second': 'name01',
#         'third': 'address01'
#     },
#     'music': {
#         'first': 'id02',
#         'second': 'name02',
#         'third': 'address02'
#     }
# }
# for demo, info in user.items():
#     print("demo_no is " + demo)
#     print(info['first'] + ' ' + info['second'] + ' ' + info['third'])

# input(）的工作原理
# message = input("you input info is ：")
# print(message)

# age = input("输入你的年龄:")
# age = int(age)
# if age > 12:
#     print("是大人了")
# else:
#     print("还是小孩子")

# while 循环
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# while标志循环
# active = True
# while active:
#     message = input("输入语句：")
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# num_test = 1
# while num_test <= 5:
#     print(num_test)
#     num_test += 1

# 使用while来处理列表和字典
# 处理列表
# demo01 = ['hello', 'hey', 'see you']
# demo02 = []
# while demo01:
#     demo02 = demo01.pop()    # 从栈顶元素循环,即最后一个元素最先出栈
#     print(demo02)

# 处理字典
# name_test_demo = {}
# polling_active = True
# while polling_active:
#     name_demo = input("input your name :")
#     response = input("input your response")
#
#     name_test_demo[name_demo] = response
#
#     repeat = input("would you input again(yes | no)")
#     if repeat == 'no':
#         polling_active = False
#
# print(name_test_demo)



