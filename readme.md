# 介绍
该python程序目的是将Koreader的Json格式笔记文件转化成适合微信读书的笔记格式, 用于导入读书笔记、众山小笔记、滴墨笔记等第三方笔记软件

# 使用教程
1. 设置Koreader的导出格式为Json
2. 将Koreader导出的Json文件放置在目录下
    目录/
    ├── input.json <==
    ├── readme.md
    └── KoreaderToWeread.py
3. 执行KoreaderToWeread.py, 程序会自动生成适配微信读书的output.txt
    目录/
    ├── input.json 
    ├── readme.md
    ├── KoreaderToWeread.py
    └── output.txt <==
