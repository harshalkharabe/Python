# What is networking?
# Networking is logical or physical link between one or more devices

# What is ip-address?
# Every system in network is identified with unique number called ip-address.
# What is portno?
# Server program inside system is identified with a unique number called
# portno
# What is protocol?

# A protocol defines set of rules and regulations for developing client and
# server program.
# Example: HTTP, FTP, TCP,…

# What is socket?
# Socket is endpoint communication between two programs within network.
# Socket is used for developing client and server programs.
# For developing network application python provides a standard module
# called “socket”. It is a default module which comes with python software. It
# provides classes for developing network applications.

# What is socket?
# Socket is endpoint communication between two programs within network.
# Socket is used for developing client and server programs.
# For developing network application python provides a standard module
# called “socket”. It is a default module which comes with python software. It
# provides classes for developing network applications.

# Networking applications are two types
# 1. Connection Oriented
# 2. Connection less
# TCP stands for transmission control protocol, it is connection oriented.

# UDP stands for User datagram protocol, it is connection less.
# class socket.socket(family=AF_INET, type=SOCK_STREAM)
# Create a new socket using the given address family, socket type
# SOCK_STREAM =&gt; TCP (Connection Oriented)
# SOCK_DGRAM =&gt; UDP (Connection less)
# socket.accept()
# Accept a connection. The socket must be bound to an address and
# listening for connections. The return value is a
# pair (conn, address) where conn is a new socket object usable to send and
# receive data on the connection, and address is the address bound to the
# socket on the other end of the connection.
# socket.bind(address)
# Bind the socket to address. The socket must not already be bound.
# socket.close()
# Mark the socket closed.
# socket.connect(address)
# Connect to a remote socket at address.
# socket.listen([backlog])
# Enable a server to accept connections
# socket.recv(bufsize)
# Receive data from the socket. The return value is a bytes object
# representing the data received.
# socket.send(bytes)
# Send data to the socket. The socket must be connected to a
# remote socket.

import socket

# scoket_obj = socket.socket()
# scoket_obj.bind(("localhost",40))
# scoket_obj.listen(2)
# print("Server is running..!")
# client_data = scoket_obj.accept()
# print("Connection Accepted..!")

# socket_obj = socket.socket()
# socket_obj.bind(("localhost",30))
# socket_obj.listen(2)
# print("Server is running..!")
# client_data = socket_obj.accept()
# print("Connected successfully..!")
# client = client_data[0]
# data = client.recv(1024)
# print(data.decode())
# msg = "Hello Client"
# client.send(msg.encode())


#mathserver
socket_obj = socket.socket()
socket_obj.bind(("localhost",35))
socket_obj.listen(2)
print("Server is running..")
client_data = socket_obj.accept()
print("Connected successfully..")
client = client_data[0]
data = client.recv(1024)
res = data.decode()
result = eval(res)
result = str(result).encode()
client.send(result)
print("Closed successfully..!")