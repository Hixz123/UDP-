import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('172.26.194.44', 12345))

while True:
    print("等待接收数据...")
    data, addr = s.recvfrom(1024)
    print(f'Received data from {addr}: {data.decode()}')
