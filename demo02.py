# 调用函数
# def hello_to():
#     print("hello world")
#
#
# hello_to()


# 向函数传递信息
# def hello_by_dell(username):
#     print(username + " output : hello world")
#
#
# hello_by_dell('dell')


# 关键字实参
# def describe_for_animal(animal_name, pet_type):
#     print(animal_name)
#     print(pet_type)
#
#
# describe_for_animal(animal_name='tom', pet_type='cat')


# 实参默认值
# def describe_for_animal(animal_name, pet_type='dog'):
#     print(animal_name)
#     print(pet_type)
#
#
# describe_for_animal(animal_name='tom')


# 具有返回值得函数
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     # print("你的全名为: " + full_name)
#     return full_name
#
#
# print("你的全名为: " + get_formatted_name('xia', 'wang'))


# 返回值是字典
# def input_name(first, last):
#     full_name = {'first': first, 'last': last}
#     # print("你的全名为: " + full_name)
#     return full_name
#
#
# name = input_name('dell', 'computer')
# print(" hello " + str(name))


# 传递列表
# def greet_users(names_list):
#     for name in names_list:
#         print("先生你好," + name.title())
#
#
# names = ['dell', 'lev', 'has']
# greet_users(names)


# 传递任意数量的实参（传递元组）
# def make_pizza(*topping):
#     print(topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 传递任意数量的实参（传递元组）
def make_pizza(first, last, **topping):
    bill = {}
    bill = {'first': first, 'last': last}
    for key, value in topping.items():
        bill[key] = value
    return bill


bill_client = make_pizza('dell', 'green', address='China', phone='10086')
print(bill_client)
