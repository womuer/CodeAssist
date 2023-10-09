# 读取文件的每一行，将每一行加上引号和逗号，然后写回文件
def add_quotes_and_commas(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # 加上引号和逗号
            line = '"' + line.rstrip('\n') + '",'
            # 写入新的行到输出文件
            outfile.write(line + '\n')

if __name__ == "__main__":
    input_file = "input.txt"  # 输入文件名
    output_file = "output.txt"  # 输出文件名

    add_quotes_and_commas(input_file, output_file)
