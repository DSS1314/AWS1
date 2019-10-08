import boto3
import tkinter
from tkinter import messagebox
import send
# 这是系统的登录界面
def awindow():
        root = tkinter.Tk()
        # 给主窗口设置标题内容
        root.title("队列消息管理器")
        root.geometry('450x200')
        inputUrl=tkinter.Variable()
        input_send = tkinter.Entry(root, width=35,textvariable=inputUrl)
        inputUrl.set("   ")#设置默认值
        def getUrl():#发送按钮响应事件
            m= inputUrl.get()
            send.send1(m)
            print(m)
        siginUp_button = tkinter.Button(root, text="发送", width=10, command=getUrl)  #
           # 完成布局
        input_send.place(x=100, y=50)  # 发送消息框的位置
           # self.login_button.place(x=140, y=235)
        siginUp_button.place(x=180, y=100)  # 发送按钮的位置
       # sigin1Up_button.place(x=270, y=100)
        root.mainloop()
        clear(input_send)

awindow()

