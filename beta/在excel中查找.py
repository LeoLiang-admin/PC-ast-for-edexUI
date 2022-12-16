"""
本文件为示例文件(with no bug), 已嵌入open_file_beta.py中
"""

import os
os.chdir(r"D:\AI\小爱\LittleAI-for-Windows11\1.8.0\beta") #ONLY FOR DEBUG!!!
import pandas as pd
from openpyxl import load_workbook
import pandas
import pandas as pd
import numpy as np


def get_coordinates(data: pandas.DataFrame, target: str):
    """
    根据要查找的目标,返回其在excel中的位置
    data: excel数据,
    target: 要查找的目标
    return: 返回坐标列表
    """
    data_list = np.array(data).tolist()
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            print(i, j, data_list[i][j], target, '\n')
            if data_list[i][j] == target:
                print("find")
                return [i + 1, j + 1]
    return []


# 读取excel文件
data = pd.read_excel('appLIST.xlsx')

# 获取其所在行和列
f = input("你要查找的玩意儿 >_")
target_string = f
# 得到坐标
coordinates = get_coordinates(data, target_string)
# 打印坐标


print(f"{target_string}在第{coordinates[0]}行,第{coordinates[1]}列")


df = pd.read_excel("appLIST.xlsx", usecols=[1])
print(df.values)


fa = input("")
if fa in str(df.values):
    print("True")

