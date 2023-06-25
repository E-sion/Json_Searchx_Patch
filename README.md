# Searchx_Patch

修改Telegram导出的频道json文件，搭配Searchx实现群组内文件名称检索功能

## 🎈介绍

由于Searchx无法检索到名称，本项目则是用偏手动的方式来修改Telegram导出的json文件，再使用Searchx导入修改后的json，以实现让bot检索的内容包括到群内文件名称。

首先读取频道导出的html文件，获取到群组内文件的名称和对应的id，写入到一个cvs表格，再读取频道导出的json文件，根据csv表格的id信息匹配到json内相同id的信息描述，再把该id对应的文件名称写入json中对该条信息描述的值。这样也就实现了检索到文件名称的效果.......~~（有点费劲😥）~~

## 🔑开始

#### 1.将频道的信息**什么都不勾选**导出，导出两次，第一次是**html**格式，第二次是**json**格式

![image-20230625211737161](C:\Users\cr\AppData\Roaming\Typora\typora-user-images\image-20230625211737161.png)

#### 2.修改 `SwithFilesName.py` ，将file的值修改为html的位置，如果导出了多个html，则运行一次改一次。这时你目录下应该有一个`文件名称和id.csv`文件，里面的内容即为你频道内的文件信息。

![image-20230625212225360](C:\Users\cr\AppData\Roaming\Typora\typora-user-images\image-20230625212225360.png)

#### 3.修改`AddTextToJson.py`，只需要将`json_filename`的值修改为你先前频道导出的json文件位置即可，修改后运行。

![image-20230625213134769](C:\Users\cr\AppData\Roaming\Typora\typora-user-images\image-20230625213134769.png)

#### 4.使用`Searchx`[导入上一步骤的](https://github.com/iyear/searchx/blob/master/docs/bot/README.zh.md)`new_data.json`,然后运行bot，也就可以检索到文件名称了。





