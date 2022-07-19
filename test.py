import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
port = 80                   # 设置端口号
 
s.connect(("http://api.bilibili.com/BV1w34y1J7Xx/web-interface/view", port))
print(s.recv(1024))
s.close()