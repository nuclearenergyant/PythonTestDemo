# 读取文件
# with open('pi_digits.txt') as f:
#     contents = f.read()
#     print(contents)


# 打开本地文件中的json文件
# import json
#
# file_path = 'D:\garbage.json.txt'
# with open(file_path, "r", encoding="utf-8") as text:
#     text_json = text.read()
#     if text_json.startswith(u'\ufeff'):
#             text_json = text_json.encode('utf8')[3:].decode('utf8')
#     # json_str = text.readline()  # 读取文件内容
#     print(text_json)
#     obj = json.loads(text_json)
#     print(type(obj))
#     for o in obj:
#         print(o)

# 读取文件的各行列表内容
# file_path = 'D:\garbage.json.txt'
# with open(file_path, "r", encoding="utf-8") as text:
#     text_demo = text.readline()
#     for text_demo_for in text_demo:
#         print(text_demo_for)

# 读取文件
# 'w'是清空该文件进行存储文件。’a‘是在文件后面进行存储文件
# with open('write_massage.txt', 'w') as f:
with open('write_massage.txt', 'a') as f:
    f.write("\nI lOVE YOU")
    # print(contents)
    print("success")
