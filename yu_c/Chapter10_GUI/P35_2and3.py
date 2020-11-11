'''2. 提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。'''
import easygui as eg
# title = "显示文本内容"
# msg = "文件【record.txt】的内容如下："
# file = open("../test_data/record.txt")
# result = eg.textbox(msg,title,text=file.read(),codebox=True)     # codebox:完全显示

'''2. 小甲鱼参考答案版'''
import os

file_path = eg.fileopenbox(default="*.txt") # 弹出选择文件对话框，记录文件的完整路径
with open(file_path) as old_file: # 高级的打开文件，自动捕捉异常，自动关闭文件
    title = os.path.basename(file_path)     # 返回path最后的文件名。若path以/或\结尾，那么就会返回空值。
    msg = "文件【%s】的内容如下：" % title
    text = old_file.read()
    text_after = eg.textbox(msg,title,text)


'''3. 在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，
则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能。
（提示：解决这道题可能需要点耐心，因为你有可能会被一个小问题卡住，但请坚持，自己想办法找到这个小问题所在并解决它！）'''
if text != text_after[:-1]:
    # textbox 的返回值会追加一个换行符
    choice = eg.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
    if choice == "覆盖保存":
        with open(file_path, "w") as old_file:
            old_file.write(text_after[:-1])
    if choice == "放弃保存":
        pass
    if choice == "另存为...":
        another_path = eg.filesavebox(default=".txt")
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, "w") as new_file:
            new_file.write(text_after[:-1])
