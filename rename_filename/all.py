import os

allpath = []
allname = []


def getallfile(path):
    allfilelist = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for f in allfilelist:
        filepath = os.path.join(path, f)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(f)
    return allpath, allname


if __name__ == "__main__":
    rootdir = "./"
    files, names = getallfile(rootdir)
    for file in files:
        print(file)
    print("-------------------------")
    for name in names:
        print(name)
