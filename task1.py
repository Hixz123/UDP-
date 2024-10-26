import socket

IP = "202.199.6.66"
PORT = 36006
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message to send: ")
    s.sendto(message.encode(), (IP, PORT))
    data,addr = s.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
