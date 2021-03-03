import os
import re


def replace_mark(buff_dir):
    for files_name in os.listdir(buff_dir):
        # 修改要替换的符号
        if len(files_name.split("-")) > 1:
            os.rename(os.path.join(buff_dir, files_name),
                      os.path.join(buff_dir, files_name.replace("-", "_")))
            # print(os.path.join(buff_dir, files_name.replace("-", "_")))


def remove_add(path):
    os.chdir(path)
    filelist = os.listdir(path)
    for filename in filelist:
        try:
            result = re.match(r"(^.*\_)(.*)", filename).group(2)

            if result:
                os.rename(filename, result)
        except Exception as e:
            pass


remove_add("./")
# replace_mark('./')
