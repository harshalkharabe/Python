import socket

# socket_obj = socket.socket()
# socket_obj.connect(("localhost",40))

# socket_obj = socket.socket()
# socket_obj.connect(("localhost",30))
# msg = "Hello Server"
# socket_obj.send(msg.encode())
# data = socket_obj.recv(1024)
# print(data.decode())

socket_obj = socket.socket()
socket_obj.connect(("localhost",35))
msg = input("Enter expression :")
socket_obj.send(msg.encode())
data = socket_obj.recv(1024)
print("Result of expression :",data.decode())