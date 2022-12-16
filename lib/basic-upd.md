# [1.8.0]

**从此版本开始，"LittleAI(for-Windows11)"将不再开源 !**



# UEFI更新

## 功能增多

新增调整全局颜色选项(保留缩进)

## 内置UEFI使用手册

位于./uefi_boot/UEFI_HELP.md


## 静音模式(uefi_boot\\\F5.txt)
暂未完成
## experiment 实验性功能(uefi_boot\\\experiment.txt)(暂未创建)
alpha(α) beta(β) ultra(ult) professional(pro)

暂未完成,默认开启



## open_file_beta(Experiment) - 正在开发
与其有关的'BUG' 

```#只有以'打开'开头的命令 才执行(因技术所限)```
### **自动列表**(参考文献)
```https://blog.csdn.net/weixin_46623003/article/details/115095820```
```https://blog.csdn.net/weixin_39815435/article/details/110397310```
```https://www.cnblogs.com/yuyanc/p/16249442.html```
```https://www.zhihu.com/question/531539009```

1.读取位于 ""start menu"" 文件夹内的所有.lnk文件,保存到beta/appLIST.xlsx

2.调用open_file_beta.py ,识别输入的字符是否包含在列表内

    包含,直接打开应用,print提示

    不包含,print错误,询问是否添加路径

        添加路径分为两种:

        1)重新扫描 ""start menu"" 文件夹的改动

        2)用户自行输入软件名称,路径等信息


已完成: 

1.list app

2.find app(name) in excel

3.find app(x,y) in excel

未完成:

1.open app(name)

2.open app(all) with "command"