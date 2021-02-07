import socket
client_con=socket.socket()
client_con.connect(('localhost',9999))
client_data='iam a client'
client_con.send(bytes(client_data,'utf-8'))
msg=client_con.recv(1024).decode()
print(msg)