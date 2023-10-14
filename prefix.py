

input_file = './snippets/c.json'  # 输入文本文件
output_file = 'prefix.txt'  # 输出文件

# 打开输入文件以及输出文件
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # 检查每一行是否包含"prefix"字段
        if "prefix" in line:
            # 如果包含，将该行去除"prefix"后写入输出文件
            line_without_prefix = line.replace("\"prefix\":", "")
            outfile.write(line_without_prefix)

print("包含'prefix'字段的行已保存到", output_file)
