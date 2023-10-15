import re

# 读取文本文件
with open("prefix.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 正则表达式匹配英文和中文
english_text = re.findall(r'[a-zA-Z]+', text)
chinese_text = re.sub(r'[a-zA-Z]+', '', text)

# 写入分开的文本到输出文件
with open("prefix_divide.txt", "w", encoding="utf-8") as file:
    file.write('\n'.join(english_text))
    file.write('\n')
    file.write(chinese_text)
