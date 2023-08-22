# 导入json和csv模块
import json
import csv

# 文件导出json
# 把result.json修改为导出的文件位置。
json_filename = r"result.json"

# 文件名称csv ，不需要更改。
csv_filename = r"文件名称和id.csv"

# 导出后的json文件
new_data = r"new_data.json"


# 读取json文件的内容，存储在一个字典中
with open(json_filename, "r", encoding='utf-8') as f:
    data = json.load(f)

# 读取csv文件的内容，存储在一个列表中
with open(csv_filename, "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    # 跳过第一行，因为它是表头
    next(reader)
    # 把每一行转换成一个元组，存储在一个列表中
    rows = list(map(tuple, reader))

# 遍历csv列表，对于每一行，获取id和title的值
for row in rows:
    id = row[0]
    title = row[1]

    int_id = int(id)
    str_title = str(title)

    # 在json字典中查找是否有相同的id
    for message in data["messages"]:
        # print(message["id"])
        # print("---------s")
        # print(id)
        if isinstance(message["text"], list):
            pass
        elif message["id"] == int_id:
            # print("datatype of num_int:", type(int_id))
            #     # 如果有相同的id，就把json字:
            # print(message["text"])
            message["text"] = str_title
            print('------------------')
            print(message["text"])

        # if message["id"] == id:
        #     # 如果有相同的id，就把json字典中对应的"text"的值修改为csv中该id对应的title内容
        #     message["text"] = title
        #     # 找到相同的id后，就跳出循环，不再继续查找
        #     break

# 用json模块把修改后的json字典写入一个新的json文件中
with open(new_data, "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
