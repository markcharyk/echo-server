import socket
import echo_client

# Socket set-up
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP
    )
address = ('127.0.0.1', 50000)
server_socket.bind(address)
server_socket.listen(1)

while True:
    conn, client_address = server_socket.accept()

    # When the server receives a message
    # send it back to the client
    message = echo_client.receive_data(conn)

    conn.sendall(message)

   # Socket tear-down
    conn.shutdown(socket.SHUT_WR)
    conn.close()
server_socket.close()
