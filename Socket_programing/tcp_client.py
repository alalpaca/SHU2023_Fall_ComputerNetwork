import socket
import tkinter as tk
from tkinter import filedialog
import threading

# 创建登录函数
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        client_socket.send(username.encode("utf-8"))
        client_socket.send(password.encode("utf-8"))
    else:
        status_label.config(text="用户名和密码不能为空")

# 创建发送文件函数
def send_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            file_contents = file.read()
            client_socket.send(file_contents.encode("utf-8"))

# 创建发送消息函数
def send_message():
    message = message_entry.get()
    if message:
        client_socket.send(message.encode("utf-8"))
        message_entry.delete(0, tk.END)  # 清空输入框

# 创建退出应用程序函数
def quit_app():
    client_socket.close()
    root.destroy()

# 创建接收消息的函数
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                chat_text.config(state=tk.NORMAL)
                chat_text.insert(tk.END, message + "\n")
                chat_text.config(state=tk.DISABLED)
        except ConnectionError:
            break

# 创建图形界面
root = tk.Tk()
root.title("客户端")

username_label = tk.Label(root, text="用户名:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="密码:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="登录", command=login)
login_button.pack()

file_button = tk.Button(root, text="发送文件", command=send_file)
file_button.pack()

message_entry = tk.Entry(root)
message_entry.pack()

message_button = tk.Button(root, text="发送消息", command=send_message)
message_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

chat_label = tk.Label(root, text="聊天消息:")
chat_label.pack()

chat_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
chat_text.pack()

quit_button = tk.Button(root, text="退出", command=quit_app)
quit_button.pack()

# 创建客户端套接字并连接到服务器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8888))

# 启动消息接收线程
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.mainloop()
