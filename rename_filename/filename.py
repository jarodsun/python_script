import os

# 设置路径
fpath = './'
# print(os.listdir(filepath))
# 获取目录下的所有文件名
names = os.listdir(fpath)
# print(len(names))
# 创建一个空列表
name = []
# 在names中遍历
for i in names:
    # 把文件名拆分为名字和后缀
    portion = os.path.splitext(i)
    # 处理后缀是doc的文件名
    if portion[1] == ".doc":
        name.append(portion[0])
    # 处理后缀是docx的文件名
    if portion[1] == ".docx":
        name.append(portion[0])

# print(len(name))

with open(file=fpath + 'name.txt', mode='w', encoding="utf-8") as f1:
    for i in range(len(name)):
        date = f1.writelines(name.pop() + '\n')
    print('Fin')
