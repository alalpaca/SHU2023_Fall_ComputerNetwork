import socket
import threading
import tkinter as tk

# 存储用户信息（示例）
user_database = {
    "wang": "1234",
    "huang": "5678",
    "zhang": "1111",
    "ruan": "2222"
}

# 存储已连接的客户端套接字和用户名的字典
connected_clients = {}

# 创建服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen(5)

# 创建图形界面
server_gui = tk.Tk()
server_gui.title("服务器")

# 创建显示客户端和消息的文本框
client_listbox = tk.Listbox(server_gui, width=30, height=10)
client_listbox.pack(padx=10, pady=10)

message_text = tk.Text(server_gui, height=10, width=40)
message_text.pack(padx=10, pady=10)

# 创建退出按钮
def quit_server():
    for client_sock in connected_clients.values():
        client_sock.close()
    server_socket.close()
    server_gui.quit()

quit_button = tk.Button(server_gui, text="退出", command=quit_server)
quit_button.pack()

# 处理客户端连接
def handle_client(client_socket, username):
    client_listbox.insert(tk.END, f"客户端账号: {username}")  # 在图形界面中显示客户端账号
    connected_clients[username] = client_socket

    # 创建关闭连接按钮
    def close_connection():
        client_sock = connected_clients.get(username)
        if client_sock:
            client_sock.close()
            client_listbox.delete(client_listbox.get(0, tk.END).index(f"客户端账号: {username}"))
            del connected_clients[username]
            close_button.destroy()  # 销毁关闭按钮

    close_button = tk.Button(server_gui, text=f"关闭连接 ({username})", command=close_connection)
    close_button.pack()

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            message_text.config(state=tk.NORMAL)
            message_text.insert(tk.END, f"{username}: {message}\n")
            message_text.config(state=tk.DISABLED)

            # 广播消息给其他客户端
            broadcast_message(username, message)
        except ConnectionError:
            break

    close_button.destroy()  # 移除关闭按钮
    client_listbox.delete(client_listbox.get(0, tk.END).index(f"客户端账号: {username}"))  # 从图形界面中移除客户端账号
    del connected_clients[username]
    client_socket.close()

# 广播消息给其他客户端
def broadcast_message(sender, message):
    for username, client_sock in connected_clients.items():
        try:
            client_sock.send(f"{sender}: {message}".encode("utf-8"))
        except ConnectionError:
            continue

# 接受客户端连接并创建线程处理
def accept_connections():
    while True:
        client, addr = server_socket.accept()
        print(f"接收到来自{addr}的连接")
        client.send("欢迎连接到服务器，请输入用户名和密码：".encode("utf-8"))

        while True:  # 循环直到用户名和密码正确
            username = client.recv(1024).decode("utf-8")
            password = client.recv(1024).decode("utf-8")

            if username in user_database and user_database[username] == password:
                client.send("登录成功！".encode("utf-8"))
                break
            else:
                client.send("用户名或密码错误！请重新输入：".encode("utf-8"))

        client_thread = threading.Thread(target=handle_client, args=(client, username))
        client_thread.start()

# 启动接受客户端连接的线程
accept_thread = threading.Thread(target=accept_connections)
accept_thread.daemon = True
accept_thread.start()

server_gui.mainloop()
