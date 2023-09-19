# SHU2023_Fall_ComputerNetwork
> The sound code and markdown of Computer Network experiments of Shanghai University of 2023



## Week02 - SocketPrograming

### Brief Introduction

- The program includes two python files: **tcp_client.py** & **tcp_server.py**
- **tcp_server.py** is the file for the server, including functions of managing login clients
  - 判断用户身份是否合法为合法用户 echo 数据 
  - 在服务器控制台可显示服务器所处状态信息并可控制关闭连接和退出
  - 设计为并发式服务器
- **tcp_client.py** is the file for clients, including following functions
  - 能通过用户名和密码登录
  - 向服务器发一文本文件或向服务器端发一段文本
  - 可实现聊天室通信
  - 用户在通信完成后可自行退出
- this program has designed GUI page


### How to use

1. Dowload the python code, and prepare the neccessary python package.

2. use python terminal to run the **tcp_server.py**

   ![image-20230919111528919](https://github.com/alalpaca/SHU2023_Fall_ComputerNetwork/blob/main/Socket_programing/images/image-20230919111528919.png)

3. the use python terminal to run the **tcp_client.py**

   <img src="https://github.com/alalpaca/SHU2023_Fall_ComputerNetwork/blob/main/Socket_programing/images/image-20230919111635004.png" alt="image-20230919111635004" style="zoom:10%;" />

   you can open multiple client windows depending on how much clients you need 

4. login in the client account using username and password(can be modified in **tcp_server.py**)

   - If login fail, the chat window will remind. You can try infinite times untill get a correct one.

     <img src="C:\Users\Kevin Wang\AppData\Roaming\Typora\typora-user-images\image-20230919112123173.png" alt="image-20230919112123173" style="zoom: 33%;" />

5. sending messages

   <img src="C:\Users\Kevin Wang\AppData\Roaming\Typora\typora-user-images\image-20230919112323332.png" alt="image-20230919112323332" style="zoom:33%;" />

6. sending files(txt)

   <img src="C:\Users\Kevin Wang\AppData\Roaming\Typora\typora-user-images\image-20230919112422703.png" alt="image-20230919112422703" style="zoom:33%;" />

   - the file can be choosed from your computer.

7. quit and connnection closed
   - the server cna actively shut down the connection of clients or quit.
   - the clients can quit actively too with the button.

