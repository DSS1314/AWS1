import boto3
import tkinter
from tkinter import messagebox
import receive
def ui1():
    root = tkinter.Tk()
    # 给主窗口设置标题内容
    root.title("队列消息管理器")
    root.geometry('450x400')
    # 创建一个`label`名为`来信: `
   # label_receive = tkinter.Label(root, text="来信： ")
    # 创建一个消息接收文本框,并设置尺寸
    def ui():  # 接收按钮响应事件
        j = receive.receive1()
        input_receive.insert("1.0", j)
        print(j)
        print("           ")
    sigin1Up_button = tkinter.Button(root, text="接收", width=10, command=ui)  # command=ui1()
    input_receive=tkinter.Text(root, height=20, width=40)
   # R = receive  # 定义receive.py的对象
    sigin1Up_button.place(x=20, y=20)  # 来信的位置
    input_receive.place(x=120, y=30)  # 收到的消息的显示位置
    root.mainloop()
ui1()