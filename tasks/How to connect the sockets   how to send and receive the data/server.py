import socket
server_con=socket.socket()

server_con.bind(('localhost',9999))
server_con.listen(3)
while True:
    client_conn,address=server_con.accept()
    print('iam connected with : ',address)
    server_data='i am a server'
    client_conn.send(bytes(server_data,'utf-8'))
    msg=client_conn.recv(1024).decode()
    print(msg)
    client_conn.close()


