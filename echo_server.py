import socket

# Socket set-up
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP
    )
address = ('127.0.0.1', 50639)
server_socket.bind(address)
server_socket.listen(1)

conn, client_address = server_socket.accept()
msg = "placeholder"

# While the server receives a non-empty message
# send it back to the client
while msg:
    msg = conn.recv(1024)
    conn.sendall(msg)

# Socket tear-down
conn.shutdown(socket.SHUT_WR)
conn.close()
server_socket.close()
