import socket
import sys

# Socket set-up
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_IP
    )
address = ('127.0.0.1', 50639)
client_socket.connect(address)

# If there is a command line argument -> get it
try:
    msg = sys.argv[1]
# If no CLA -> prompt for a message
except IndexError:
    msg = raw_input("> ")

# Keep prompting for input and sending it off to the server
# as long as msg has something in it
while msg:
    client_socket.sendall(msg)
    msg = client_socket.recv(1024)
    print msg
    msg = raw_input("> ")

# Socket tear-down
client_socket.shutdown(socket.SHUT_WR)
client_socket.close()
