'''
Author: Eric Jiang
Date: 2024-03-16
From: https://github.com/Ericjsz/KoreadertoWeread
'''


import os
import json

# 获取当前脚本所在目录的路径
directory = os.path.dirname(os.path.realpath(__file__))

# 列出目录中所有的JSON文件
json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

# 检查是否只有一个JSON文件
if len(json_files) != 1:
    raise Exception("错误: 目录中应该只有一个JSON文件。")

# 读取JSON文件
json_file_path = os.path.join(directory, json_files[0])
with open(json_file_path, 'r') as file:
    data = json.load(file)

# 根据给定模板格式化数据
output_content = f"{data['title']}\n{data['author']}\n{len(data['entries'])}个笔记\n\n"

# 跟踪章节以避免重复
chapters_included = set()

for entry in data['entries']:
    if entry['chapter'] not in chapters_included:
        output_content += f"\n◆  {entry['chapter']}\n\n"
        chapters_included.add(entry['chapter'])
    output_content += f">> {entry['text']}\n\n"

# 将格式化的内容保存到输出文件
output_file_path = os.path.join(directory, 'output.txt')
with open(output_file_path, 'w') as output_file:
    output_file.write(output_content)

# 输出创建文件的路径
print(f"输出文件已创建在: {output_file_path}")
