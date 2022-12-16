"""
此文件为示例文件(no bug),已嵌入open_file_beta中
"""
import os
os.chdir(r"D:\AI\小爱\LittleAI-for-Windows11\1.8.0\beta") #ONLY FOR DEBUG!!!
import pandas as pd
from openpyxl import load_workbook
workbook = load_workbook(filename='appLIST.xlsx')
sheet = workbook.active


# 定义函数
def list_all_files(rootdir):
    import os
    _files = []
    # 列出文件夹下所有的目录与文件
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        # 构造路径
        path = os.path.join(rootdir, list[i])
        # 判断路径是否为文件目录或者文件
        # 如果是目录则继续递归
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

# 执行
dir = r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs' # 目录地址
# list_all_files(dir)


datatx = pd.DataFrame(list_all_files(dir))
datatx.to_excel('appLIST.xlsx')