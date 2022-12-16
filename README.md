# PC-AST-FOR-eDEXUI

# 为‘eDEXUI’开源项目而适配的电脑助手

效果：![](https://s3.bmp.ovh/imgs/2022/12/16/5799092c5535c3ef.png)

由Little-AI-For-Windows11演变而来

适配了eDEX-UI的风格，能在eDEX-UI中流畅运行，让操作变得更具有科技感

1.0版本挺简陋的，只支持打开软件、网页

## 如何启动

在edexUI中用python运行index.py

若目录不在remix-1.0下，则先需要cd到该目录

![](https://s3.bmp.ovh/imgs/2022/12/16/c8a67a1051ab73d3.png)

直接按enter(**ctrl+L的debug-mod还在1.8.0没有移植过来**，算是主动阉割了)

启动中有一个动画，文字懒得改了，有音效

![](https://s3.bmp.ovh/imgs/2022/12/16/a779a30d29bf692b.png)

完事儿以后就可以直接输入命令了(**两个MOD是被阉割掉的功能，目前不用管他**，到后面可能会移植过来)![](https://s3.bmp.ovh/imgs/2022/12/16/020b7c32f4d1ad4c.png)

## 主要功能

#### 1.打开软件

直接键入run + 程序名**[千万不要加后缀(类似于.lnk .exe)]**

```shell
run wechat
```

如果打印出了True和文件(快捷方式)路径，说明成功了

输出：

![](https://s3.bmp.ovh/imgs/2022/12/16/eca21312ba8bf891.png)

**目前只支持在C:\ProgramData\Microsoft\Windows\Start Menu\Programs里面创建过快捷方式的软件**

#### 2.清屏

与cmd相同，直接键入'cls'即可，**区分大小写**



## 问题解决

### 1.run相关(报错&BUG)

**！！****初次使用需要先list app**

为什么找不到我想要打开的app？甚至报错？

![](https://s3.bmp.ovh/imgs/2022/12/16/50c571f7f7775cfa.png)

报错分两种：

1.找不到该名称在excel中的坐标（如上图所示）

2.找不到excel文件的位置（**初次使用会出现**）

如果你确信输入的软件名称在此目录创建过快捷方式，请尝试重新获取列表（同样适用于第二种报错）

```
list app
```

![](https://s3.bmp.ovh/imgs/2022/12/16/5981ce0cda224021.png)

这些会自动保存到index.py同目录下的appLIST.xlsx，方便run时调用

### 2.其他(错误的命令)

![](https://s3.bmp.ovh/imgs/2022/12/16/032589eee7ed2eda.png)

原因：该命令有错/暂不支持