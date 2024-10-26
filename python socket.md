# Python Socket（客户端）的部分应用

> 以下大部分内容学自廖雪峰的博客

## 概念

1. Socket:“套接字”。是计算机之间进行通信的一种约定或方式。可以理解为socket也是一种特殊的文件，一些socket函数是对其进行操作（读写、打开、关闭）Socket()函数返回的是一个整型的Socket描述符，随后的建立、数据传输等操作都是通过Socket实现的。
2. 创建TCP/UDP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

## 基本用法

> 由于TCP和UDP上部分python代码不同，这里只说一下与题目相关的UDP写法

1. 导入socket库，并创建一个socket，由此建立起链接

   ```python
   import socket
   
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   #socket.AF_INET和socket.SOCK_STREAM代表创建的socket的参数。
   #如AF_INET表示指定使用IPv4协议，想用IPv6的话可以这样写：AF_INET6
   #SOCK_DGRAM指定使用面向流的UDP协议，想用TCP协议的话可以这样写：SOCK_STREAM
   #注意参数是一个元组！
   
   s.connect(('IP地址', '端口号'))
   ```

2.持续的接收数据

```python
#写一个循环，保持持续接受
While True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
    
#data, addr = s.recvfrom(1024)中
#recvfrom(1024) 方法用于从套接字接收数据。它会阻塞，直到有数据到达。1024 是接收缓冲区的大小，单位是字节
#data 是接收到的数据，类型是字节串（bytes）。
#addr 是发送数据的客户端的地址和端口，类型是元组（tuple），包含两个元素：IP地址（字符串）和端口号（整数）。
#print('Received from %s:%s.' % addr),%s:%s 是格式化字符串，用于将 addr 元组中的两个元素插入到字符串中。实际效果就是Received from IP地址:端口号
#s.sendto(b'Hello, %s!' % data, addr),"b"表示转化为bytes字节串而非str字符串
#用bytes与IO编程有关，有以下好处： 1.二进制数据的精确表示，避免数据的失真或错误解释 2.避免编码问题（在Python中默认使用Unicode编码）3.跨平台兼容性......
#最后一个addr表示客户端的地址和端口，用于指定消息的目的地。
```

