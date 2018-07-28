#! python3
# This server is for reflecting back messages sent from a client
import socket
import threading
import argparse


def server_setup(bind_port, bind_ip='0.0.0.0', max_conn=5):
    # Instantiate server object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the IP address desired and port
    # NOTE: port must be an integer and IP addr must be string
    server.bind((bind_ip, bind_port))

    # Set maximum number of connections
    server.listen(max_conn)

    print(f"[*] Listeing on {bind_ip}:{bind_port}")

    return server


# This is the client-handling thread
def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(1024)
    print('[*] Received: {}'.format(request.decode('utf-8')))

    # Send a packet back
    client_socket.send('ACK!'.encode('utf-8'))

    client_socket.close()


reflect_server = server_setup(9999)

try:
    while True:
        client, addr = reflect_server.accept()

        print(f'[*] Accepted connection from: {addr[0]}:{addr[1]}')

        # Start thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
except KeyboardInterrupt:
    print('\n[*] Server halted')
