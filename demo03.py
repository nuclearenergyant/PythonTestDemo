# 异常-处理算法异常
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

# 异常-处理文件未找到异常
# fileName = 'alice.txt'
# try:
#     with open(fileName) as demo:
#         content = demo.read()
#         print(content)
# except FileNotFoundError:
#     print("Don't have this file")


# 存储文件
# 读取文件json.load()和写文件列表json.dump()
import json
number = [1, 2, 3, 4, 5, 6]
fileName = 'number.json'
with open(fileName, 'w') as f_obj:
    json.dump(number, f_obj)

with open(fileName) as demo_file:
    numbers = json.load(demo_file)
print(numbers)
