import json

# 读取包含JSON数据的文件
with open('./snippets/bash_sn.json', 'r') as file:
    data = json.load(file)

# 修改JSON对象中的prefix值
for key, value in data.items():
    if "prefix" in value:
        prefix = value["prefix"]
        if isinstance(prefix, str):
            value["prefix"] = "bash " + prefix
        elif isinstance(prefix, list):
            value["prefix"] = ["bash " + p for p in prefix]

# 获取修改后的prefix的值
modified_prefix_values = [value["prefix"] for value in data.values()]

# 保存修改后的prefix值到txt文件
with open('prefix_bash.txt', 'w') as txt_file:
    for prefix_value in modified_prefix_values:
        if isinstance(prefix_value, str):
            txt_file.write(prefix_value + '\n')
        elif isinstance(prefix_value, list):
            txt_file.writelines([prefix + '\n' for prefix in prefix_value])
